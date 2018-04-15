#This is the abstraction for the states in the machine


class State:
    #initializes each state with a Game object
    def __init__(self, stateName, Game):
        self.game = Game;
        self.name = stateName
    #sets the next state
    def setNextState(self, state, Game):
        return
    #processes the current state
    def processCurrent(self, Game):
        return

