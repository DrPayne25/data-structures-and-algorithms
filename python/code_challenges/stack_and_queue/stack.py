from code_challenges.stack_and_queue.node import Node

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def isEmpty(self):
        return self.top == None

    def pop(self):
        if self.isEmpty():
            raise Exception('Trying to pop from an empty stack')
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.size -= 1
        return temp.value

    def size(self):
        return self.size

    def peek(self):
        if self.isEmpty():
            raise Exception('Trying to peek from an empty stack')
        return self.top.value
