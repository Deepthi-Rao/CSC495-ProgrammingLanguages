import socket, threading

threads = []

def threadMain(cs, addr):
    msg = ''
    pkt = cs.recv(2048)
    while pkt != b'':
        msg += str(pkt, encoding='utf-8')
        if msg[-1] == '\n':
            print(msg)
            msg = ''
        pkt = cs.recv(2048)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 2222))
    s.listen(5)
    while True:
        (cs, addr) = s.accept()
        t = threading.Thread(target=threadMain, args=(cs, addr))
        threads.append(t)
        t.start()

# vim: set filetype=python ts=4 sw=4 expandtab:
