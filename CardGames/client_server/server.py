import argparse
import socket, threading
from nettools import *
import sys
sys.path.insert(1,'../utils')
import queue
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
clientGetter = None
clientSender = None
gameThread = None
gameMaster = None
gmLock = threading.Lock()
clientThreads = []
game = None
# The queue of messages for the game to handle
gameQueue = queue.Queue()
# The queue of messages for the server to handle
responseQueue = queue.Queue()
# Event for when the server puts a message in the queue for the game to handle
serverEvent = threading.Event()
# Event for when the game puts a message in the queue for the server to handle
responseEvent = threading.Event()

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
                    msgQueue.enqueue((clientGetter, 'CONNECT ' + self.playerName))
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
            msgQueue.enqueue((clientGetter, 'DISCONNECT ' + self.playerName))
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
        msgQueue.enqueue((clientGetter, 'MASTER ' + client.playerName))
        msgEvent.set()
    else:
        print('Game Master is no longer set')

def handleAdminMsg(msg):
    tokens = msg.split(' ')
    if tokens[0] == 'CONNECT':
        otherPlayers = [c.playerName for c in clientThreads if c.playerName != tokens[1]]
        responseQueue.enqueue((otherPlayers, '{}: {} has connected'.format(ADMIN, tokens[1])),
                ([tokens[1]], ADMIN + ': ' + (('Current players are: ' + ', '.join(otherPlayers)) if len(otherPlayers) else 'No other players')))
    elif tokens[0] == 'DISCONNECT':
        otherPlayers = [c.playerName for c in clientThreads if c.playerName != tokens[1]]
        responseQueue.enqueue((otherPlayers, '{}: {} has disconnected'.format(ADMIN, tokens[1])))
    elif tokens[0] == 'MASTER':
        allPlayers = [c.playerName for c in clientThreads]
        responseQueue.enqueue((allPlayers, '{}: {} is now the Game Master'.format(ADMIN, tokens[1])))
    else:
        print('unknown ' + ADMIN + ' msg: ' + msg)

def handleGMCmdMsg(msg):
    global game
    global running
    if msgArgs[0].upper() == CMDSTART:
        if len(msgArgs) <= 1:
            responseQueue.enqueue(([playerName], 'Invalid command'))
        elif msgArgs[1].upper() in ERSNAME:
            listener.close()
            game = EgyptianRatsCrew([c.playerName for c in clientThreads], (gameQueue, serverEvent), (responseQueue, responseEvent))
            responseQueue.enqueue(([c.playerName for c in clientThreads], 'Starting Egyptian Rat Screw.'))
            gameThread = threading.Thread(target=game.run())
            gameThread.start()
        elif msgArgs[1].upper() in LASTONENAME:
            responseQueue.enqueue(([c.playerName for c in clientThreads], 'Last One not server compatible.'))
    elif msgArgs[0].upper() == CMDHALT:
        running = False

def handleCmdMsg(name, msg):
    msgArgs = msg.split(' ')
    if name == gameMaster.playerName:
        handleGMCmdMsg(msg)
    else:
        responseQueue.enqueue(([name], 'Invalid command'))

def processMsg(name, msg):
    if len(msg) == 0:
        return
    elif name == ADMIN:
        handleAdminMsg(msg)
    elif msg[0] == CMDLEADER:
        handleCmdMsg(name, msg)
    elif game and game.name == 'Egyptian Rats Crew':
        gameQueue.enqueue((name, msg))
    else:
        responseQueue.enqueue(([c.playerName for c in clientThreads if c.playerName != name], name + ': ' + msg))

def clientSenderMain():
    while running:
        responseEvent.wait()
        responseEvent.clear()
        while responseQueue.notEmpty():
            response = responseQueue.dequeue()
            print(response[1])
            for c in clientThreads:
                if c.playerName in response[0]:
                    c.send(response[1])

def clientGetterMain():
    while running:
        msgEvent.wait()
        msgEvent.clear()
        while msgQueue.notEmpty():
            msg = msgQueue.dequeue()
            processMsg(msg[0].playerName, msg[1])

if __name__ == "__main__":
    args = cmdline()
    clientGetter = threading.Thread(target=clientGetterMain)
    clientGetter.playerName = ADMIN
    clientGetter.start()
    clientSender = threading.Thread(target=clientSenderMain)
    clientSender.playerName = ADMIN
    clientSender.start()
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
    clientGetter.join()
    clientSender.join()
    gameThread.join()
    print('Shutting down')
    for t in clientThreads:
        t.exit()

# vim: set filetype=python ts=4 sw=4 expandtab:
