import sys,re,traceback,time,random
from game_abstractions.game import Game
from machine_abstractions.state import State

#This class creates the abstraction for the general machines
class Machine:

    # this initializes a machine
    def __init__(self, Game):
        self.game = Game
        self.canAct = False; #can the player act at the beginning, no
        self.states = {}
        self.actions = []

    def addAction(self, action):
        self.actions.append(action)

    def handleMsg(msg):
        for action in self.actions:
            action(msg)

    # this creates a state
    def createState(self, stateName):
        if isinstance(stateName, State):
            return stateName
        self.states.add(State(stateName, self.game));
        return State(stateName, self.game)

    # this sets the current State
    def setCurrentState(self, state):
        self.currentState = state;

    #this gets the current State
    def getCurrentState(self):
        return self.currentState







