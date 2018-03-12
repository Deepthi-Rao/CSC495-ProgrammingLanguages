import sys, traceback, time, random

class Player:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, id):
        self.id = id
    
    def getId(self):
        return self.id

    def setIsPlaying(self, isPlaying):
        self.isPlaying = isPlaying;

    def getIsPlaying(self):
        return self.isPlaying
