import argparse
import socket, threading
from EgyptianRatsCrew import EgyptianRatsCrew

ADMIN = 'Server'
MIN_NAME_LENGTH = 2
INVALID_NAMES = [ADMIN.upper(), 'SERVER', 'ADMIN', 'OWNER', 'SYSTEM']
CMDLEADER = '/'
CMDSTART = CMDLEADER + 'START'
CMDHALT = CMDLEADER + 'HALT'

ERSNAME = ['ERS', 'EGYPTIANRATSCREW']
LASTONENAME = ['LO', 'LASTONE']

listener = None
controller = None
gameMaster = None
gmLock = threading.Lock()
clientThreads = []
msgQueue = []
msgEvent = threading.Event()
running = True
game = None

def cmdline():
    parser = argparse.ArgumentParser(description='Game server')
    parser.add_argument('-p', '--port', type=int, default=2222, help='server port number')
    return parser.parse_args()

class Client(threading.Thread):
    def __init__(self, cs, addr):
        super().__init__()
        self.cs = cs
        self.addr = addr
        self.playerName = ''
        self.nameset = False

    def run(self):
        self.send('Input player name')
        msg = ''
        pkt = self.cs.recv(2048)
        while pkt != b'':
            msg += str(pkt, encoding='utf-8')
            if msg[-1] == '\n':
                if self.nameset == False:
                    if self.setName(msg[:-1]):
                        print('{} has name {}'.format(self.addr, self.playerName))
                        msgQueue.append((controller, 'CONNECT ' + self.playerName))
                        msgEvent.set()
                    else:
                        self.send('Invalid player name. Enter a new one')
                else:
                    msgQueue.append((self, msg[:-1]))
                    msgEvent.set()
                msg = ''
            pkt = self.cs.recv(2048)
        self.cs.shutdown(socket.SHUT_RDWR)
        self.cs.close()
        print('{} ({}) has disconnected'.format(self.addr, self.playerName))
        if running:
            msgQueue.append((controller, 'DISCONNECT ' + self.playerName))
            msgEvent.set()
        clientThreads.remove(self)
        with gmLock:
            if gameMaster == self:
                setGameMaster(None)
                for c in clientThreads:
                    if c.nameset:
                        setGameMaster(c)
                        break

    def setName(self, name):
        name = name.strip()
        if len(name) < MIN_NAME_LENGTH or name.upper() in INVALID_NAMES: 
            return False
        for c in clientThreads:
            if c.playerName.upper() == name.upper():
                return False
        self.playerName = name
        self.nameset = True
        with gmLock:
            if gameMaster == None:
                setGameMaster(self)
        return True

    def send(self, msg):
        msg = msg + '\n'
        charssent = 0
        while charssent < len(msg):
            try:
                sent = self.cs.send(msg[charssent:].encode(encoding='utf-8'))
            except (BrokenPipeError, OSError):
                sent = 0
            if sent == 0:
                return
            charssent += sent

    def exit(self):
        self.cs.shutdown(socket.SHUT_WR)

def setGameMaster(client):
    # setGameMaster must be called within "with gmLock"
    global gameMaster
    gameMaster = client
    if client != None:
        print('{} is now the Game Master'.format(client.playerName))
        msgQueue.append((controller, 'MASTER ' + client.playerName))
        msgEvent.set()
    else:
        print('Game Master is no longer set')

def processMsg(name, msg):
    global running
    global game
    if name == ADMIN:
        tokens = msg.split(' ')
        if tokens[0] == 'CONNECT':
            otherPlayers = [c.playerName for c in clientThreads if c.playerName != tokens[1]]
            return [(otherPlayers, '{}: {} has connected'.format(ADMIN, tokens[1])),
                    ([tokens[1]], ADMIN + ': ' + (('Current players are: ' + ', '.join(otherPlayers)) if len(otherPlayers) else 'No other players'))]
        elif tokens[0] == 'DISCONNECT':
            otherPlayers = [c.playerName for c in clientThreads if c.playerName != tokens[1]]
            return [(otherPlayers, '{}: {} has disconnected'.format(ADMIN, tokens[1]))]
        elif tokens[0] == 'MASTER':
            allPlayers = [c.playerName for c in clientThreads]
            return [(allPlayers, '{}: {} is now the Game Master'.format(ADMIN, tokens[1]))]
        else:
            print('unknown ' + ADMIN + ' msg: ' + msg)
        return []

    if len(msg) == 0:
        return []
    if msg[0] == CMDLEADER:
        msgArgs = msg.split(' ')
        if msgArgs[0].upper() == CMDSTART and name == gameMaster.playerName:
            if len(msgArgs) <= 1:
                return [([name], 'Invalid command')]
            if msgArgs[1].upper() in ERSNAME:
                listener.close()
                game = EgyptianRatsCrew([c.playerName for c in clientThreads])
                return [([c.playerName for c in clientThreads], 'Starting Egyptian Rat Screw.')]
            elif msgArgs[1].upper() in LASTONENAME:
                listener.close()
                return [([c.playerName for c in clientThreads], 'Starting Last One.')]
        if msgArgs[0].upper() == CMDHALT and name == gameMaster.playerName:
            running = False
            return []
        return [([name], 'Invalid command')]
    if game:
        return game.play()
    return [([c.playerName for c in clientThreads if c.playerName != name], name + ': ' + msg)]

def controllerMain():
    while running:
        msgEvent.wait()
        msgEvent.clear()
        while len(msgQueue) > 0:
            msg = msgQueue.pop(0)
            responseList = processMsg(msg[0].playerName, msg[1])
            for r in responseList:
                print(r[1])
                for c in clientThreads:
                    if c.playerName in r[0]:
                        c.send(r[1])

if __name__ == "__main__":
    args = cmdline()
    controller = threading.Thread(target=controllerMain)
    controller.playerName = ADMIN
    controller.start()
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind((socket.gethostname(), args.port))
    print('Hostname: {}'.format(socket.gethostname()))
    print('Port: {}'.format(args.port))
    listener.listen(5)
    while running:
        cs = None
        try:
            cs, addr = listener.accept()
            print('New connection from {}'.format(addr))
            t = Client(cs, addr)
            clientThreads.append(t)
            t.start()
        except KeyboardInterrupt:
            if cs:
                cs.close()
            listener.close()
            running = False
            msgEvent.set()
        except OSError:
            if cs:
                cs.close()
            break
    controller.join()
    print('Shutting down')
    for t in clientThreads:
        t.exit()

# vim: set filetype=python ts=4 sw=4 expandtab:
