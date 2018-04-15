import random

#This is the abstraction for a stack that will be used to define properties of a deck and a pile
class Stack():

    #initializes the stack
    def __init__(self):
        self.stack = []
        self.size = 0

    #places an element on the stack
    def push(self, item):
        self.stack.append(item)
        self.size += 1

    #removes an element from the stack
    def pop(self):
        self.size -= 1
        return self.stack.pop()

    #returns the first element on the stack
    def peekFirst(self):
        return self.stack[self.size-1]

    #returns the second element on the stack
    def peekSecond(self):
        return self.stack[self.size-2]

    #returns the third element on the stack
    def peekThird(self):
        return self.stack[self.size-3]

    #shuffles the stack
    def shuffle(self):
        random.shuffle(self.stack)