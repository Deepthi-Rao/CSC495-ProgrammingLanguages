import socket, threading

ADMIN = 'Server'
controller = None
clientThreads = []
msgQueue = []
msgEvent = threading.Event()

class Client(threading.Thread):
    def __init__(self, cs, addr):
        super().__init__()
        self.cs = cs
        self.addr = addr
        self.playerName = ''
        self.nameset = False

    def run(self):
        msg = ''
        pkt = self.cs.recv(2048)
        while pkt != b'':
            msg += str(pkt, encoding='utf-8')
            if msg[-1] == '\n':
                if self.nameset == False:
                    self.setName(msg[:-1])
                    print('{} has name {}'.format(self.addr, self.playerName))
                    msgQueue.append((controller, '{} has connected'.format(self.playerName)))
                    msgEvent.set()
                else:
                    msgQueue.append((self, msg[:-1]))
                    msgEvent.set()
                msg = ''
            pkt = self.cs.recv(2048)
        print('{} ({}) has disconnected'.format(self.addr, self.playerName))
        msgQueue.append((controller, '{} has disconnected'.format(self.playerName)))
        msgEvent.set()
        clientThreads.remove(self)

    def setName(self, name):
        self.playerName = name
        self.nameset = True

    def send(self, msg):
        msg = msg + '\n'
        charssent = 0
        while charssent < len(msg):
            try:
                sent = self.cs.send(msg[charssent:].encode(encoding='utf-8'))
            except BrokenPipeError:
                sent = 0
            if sent == 0:
                return
            charssent += sent

def processMsg(name, msg):
    if name == ADMIN:
        who = msg.split(' ')[0]
        otherPlayers = [c.playerName for c in clientThreads if c.playerName != who]
        return [(otherPlayers, ADMIN + ': ' + msg),
                (who, ADMIN + ': ' + (('Current players are: ' + ', '.join(otherPlayers)) if
len(otherPlayers) else 'No other players'))]
    return [([c.playerName for c in clientThreads if c.playerName != name], name + ': ' + msg)]

def controllerMain():
    while True:
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
    controller = threading.Thread(target=controllerMain)
    controller.playerName = ADMIN
    controller.start()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 2222))
    print('Hostname: {}'.format(socket.gethostname()))
    print('Port: {}'.format(2222))
    s.listen(5)
    while True:
        (cs, addr) = s.accept()
        print('New connection from {}'.format(addr))
        t = Client(cs, addr)
        clientThreads.append(t)
        t.start()

# vim: set filetype=python ts=4 sw=4 expandtab:
