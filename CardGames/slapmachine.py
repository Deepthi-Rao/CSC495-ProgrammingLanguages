#!/usr/local/bin/python3

import sys, traceback, time, random

class State:
    def __repr__():
        return self.__name__
    
class Slappable(State):
    def onSlap(self):
        print("Collect all played cards.")
    
class NonSlappable(State):
    def onSlap(self):
        print("Discard two cards.")