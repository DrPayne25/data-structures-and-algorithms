from code_challenges.stack_and_queue.node import Node

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    # different way to do enqueue
    # def enqueue(self, value):
    #     node = Node(value)
    #     if self.rear:
    #         self.rear.next = node
    #     self.rear = node
    #     self.front = self.front or self.rear


    def dequeue(self):
        if self.front == None:
            raise Exception('Trying dequeue a empty queue')
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.isEmpty():
            raise Exception('Trying to peek from an empty queue')
        return self.front.value

