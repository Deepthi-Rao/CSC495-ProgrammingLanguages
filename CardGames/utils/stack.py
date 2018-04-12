import random

class Stack():
    
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
        
    def pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def peek(self):
        return self.stack[self.size-1]
    
    def shuffle(self):
        random.shuffle(self.stack)