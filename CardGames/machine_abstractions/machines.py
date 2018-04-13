class Machine:
    def __init__(self):
        self.actions = []

    def addAction(self, action):
        self.actions.append(action)

    def handleMsg(msg):
        for action in self.actions:
            action(msg)

class AsynchronousMachine(Machine):

