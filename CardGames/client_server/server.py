import argparse
import socket, threading
from nettools import *
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
game = None

def cmdline():
    parser = argparse.ArgumentParser(description='Game server')
    parser.add_argument('-p', '--port', type=int, default=2222, help='server port number')
    return parser.parse_args()

class Client(CommThread):
    def __init__(self, sock, addr):
        super().__init__(sock)
        self.addr, self.playerName, self.nameset = addr, '', False

    def run(self):
        self.send('Input player name')
        msg = self.receive()
        while msg:
            if self.nameset == False:
                if self.setName(msg):
                    print('{} has name {}'.format(self.addr, self.playerName))
                    msgQueue.enqueue((controller, 'CONNECT ' + self.playerName))
                    msgEvent.set()
                else:
                    self.send('Invalid player name. Enter a new one')
            else:
                msgQueue.enqueue((self, msg))
                msgEvent.set()
            msg = self.receive()
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        print('{} ({}) has disconnected'.format(self.addr, self.playerName))
        if running:
            msgQueue.enqueue((controller, 'DISCONNECT ' + self.playerName))
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

    def exit(self):
        self.sock.shutdown(socket.SHUT_WR)

def setGameMaster(client):
    # setGameMaster must be called within "with gmLock"
    global gameMaster
    gameMaster = client
    if client != None:
        print('{} is now the Game Master'.format(client.playerName))
        msgQueue.enqueue((controller, 'MASTER ' + client.playerName))
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
                return [([c.playerName for c in clientThreads], 'Last One not server compatible.')]
        if msgArgs[0].upper() == CMDHALT and name == gameMaster.playerName:
            running = False
            return []
        return [([name], 'Invalid command')]
    if game and game.name == 'Egyptian Rats Crew':
        return game.play()
        return game.processMsg(name, msg)
    return [([c.playerName for c in clientThreads if c.playerName != name], name + ': ' + msg)]

def controllerMain():
    while running:
        msgEvent.wait()
        msgEvent.clear()
        while msgQueue.notEmpty():
            msg = msgQueue.dequeue()
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
        sock = None
        try:
            sock, addr = listener.accept()
            print('New connection from {}'.format(addr))
            t = Client(sock, addr)
            clientThreads.append(t)
            t.start()
        except KeyboardInterrupt:
            if sock:
                sock.close()
            listener.close()
            running = False
            msgEvent.set()
        except OSError:
            if sock:
                sock.close()
            break
    controller.join()
    print('Shutting down')
    for t in clientThreads:
        t.exit()

# vim: set filetype=python ts=4 sw=4 expandtab:
