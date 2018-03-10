import argparse
import socket, threading

ADMIN = 'Server'
MIN_NAME_LENGTH = 2
INVALID_NAMES = [ADMIN.upper(), 'SERVER', 'ADMIN', 'OWNER', 'SYSTEM']
controller = None
clientThreads = []
msgQueue = []
msgEvent = threading.Event()
running = True

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
                        msgQueue.append((controller, '{} has connected'.format(self.playerName)))
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
            msgQueue.append((controller, '{} has disconnected'.format(self.playerName)))
            msgEvent.set()
        clientThreads.remove(self)

    def setName(self, name):
        name = name.strip()
        if len(name) < MIN_NAME_LENGTH or name.upper() in INVALID_NAMES: 
            return False
        for c in clientThreads:
            if c.playerName.upper() == name.upper():
                return False
        self.playerName = name
        self.nameset = True
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

def processMsg(name, msg):
    if name == ADMIN:
        who = msg.split(' ')[0]
        otherPlayers = [c.playerName for c in clientThreads if c.playerName != who]
        return [(otherPlayers, ADMIN + ': ' + msg),
                (who, ADMIN + ': ' + (('Current players are: ' + ', '.join(otherPlayers)) if
len(otherPlayers) else 'No other players'))]
    return [([c.playerName for c in clientThreads if c.playerName != name], name + ': ' + msg)]

def controllerMain():
    while running:
        msgEvent.wait()
        msgEvent.clear()
        while len(msgQueue) > 0:
            msg = msgQueue.pop()
            responseList = processMsg(msg[0].playerName, msg[1])
            for r in responseList:
                for c in clientThreads:
                    if c.playerName in r[0]:
                        c.send(r[1])

if __name__ == "__main__":
    args = cmdline()
    controller = threading.Thread(target=controllerMain)
    controller.playerName = ADMIN
    controller.start()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), args.port))
    print('Hostname: {}'.format(socket.gethostname()))
    print('Port: {}'.format(args.port))
    s.listen(5)
    while running:
        cs = None
        try:
            cs, addr = s.accept()
            print('New connection from {}'.format(addr))
            t = Client(cs, addr)
            clientThreads.append(t)
            t.start()
        except KeyboardInterrupt:
            if cs:
                cs.close()
            running = False
            msgEvent.set()
    s.close()
    print('Shutting down')
    for t in clientThreads:
        t.exit()

# vim: set filetype=python ts=4 sw=4 expandtab:
