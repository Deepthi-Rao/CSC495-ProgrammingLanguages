#This is the abstraction for the state class
class State:
    def __init__(self, Game):
        self.Game = Game;

    def setNextState(self, state, Game):
        return

    def processCurrent(self, Game):
        return
