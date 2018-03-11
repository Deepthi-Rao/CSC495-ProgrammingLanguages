import argparse
import sys
import socket, threading

msgQueue = []
msgEvent = threading.Event()
running = True

def cmdline():
    parser = argparse.ArgumentParser(description='Game client')
    parser.add_argument('hostname', help='server host name')
    parser.add_argument('port', nargs='?', type=int, default=2222, help='server port number')
    return parser.parse_args()

class Listener(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        global running
        msg = ''
        pkt = self.sock.recv(2048)
        while pkt != b'':
            msg += str(pkt, encoding='utf-8')
            if msg[-1] == '\n':
                msgQueue.append(msg[:-1])
                msgEvent.set()
                msg = ''
            pkt = self.sock.recv(2048)
        self.sock.close()
        if running:
            running = False
            msgQueue.append('Server connection lost. Press ENTER to exit.')
            msgEvent.set()

    def send(self, msg):
        msg = msg + '\n'
        charssent = 0
        while charssent < len(msg):
            try:
                sent = self.sock.send(msg[charssent:].encode(encoding='utf-8'))
            except (BrokenPipeError, OSError):
                sent = 0
            if sent == 0:
                return
            charssent += sent

def controllerMain():
    while running:
        msgEvent.wait()
        msgEvent.clear()
        while len(msgQueue) > 0:
            print(msgQueue.pop())

if __name__ == "__main__":
    args = cmdline()
    controller = threading.Thread(target=controllerMain)
    controller.start()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.hostname, args.port))
    listener = Listener(sock)
    listener.start()
    for line in sys.stdin:
        if not running:
            break
        if len(line) > 0 and line[-1] == '\n':
            line = line[:-1]
        if line == 'exit':
            break
        listener.send(line)
    if running:
        running = False
        msgEvent.set()
        sock.shutdown(socket.SHUT_WR)

# vim: set filetype=python ts=4 sw=4 expandtab:
