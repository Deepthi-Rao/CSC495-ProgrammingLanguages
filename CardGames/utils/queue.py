#This is the Queue class
class Queue:

    #this initializes the queue object
    def __init__(self):
        self.queue = []
        self.size = 0

    #this enqueues an element to the end of the list
    def enqueue(self, element):
        self.queue.__add__(element)
        self.size = self.size + 1

    #this dequeues an element from the front of the list
    def dequeue(self):
        self.queue.remove(0)
        self.size = self.size - 1
