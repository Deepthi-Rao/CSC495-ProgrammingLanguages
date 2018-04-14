import collections import deque

#This is the Queue class
class Queue:

    #this initializes the queue object
    def __init__(self):
        self.queue = deque([])

    #this enqueues an element to the end of the list
    def enqueue(self, element):
        self.queue.append(element)

    #this dequeues an element from the front of the list
    def dequeue(self):
        return self.queue.popleft()

    def notEmpty(self):
        return len(self.queue) > 0
