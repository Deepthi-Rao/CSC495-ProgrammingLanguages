#!/usr/local/bin/python3

import sys, traceback, time, random

class State():
    return
    
class Slappable(State):
    def onSlap(self):
        print("Collect all played cards.")
    
class NonSlappable(State):
    def onSlap(self):
        print("Discard two cards.")