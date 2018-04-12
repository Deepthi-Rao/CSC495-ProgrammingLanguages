class CommThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def receive(self):
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
