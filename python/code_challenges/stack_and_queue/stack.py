from code_challenges.stack_and_queue.node import Node

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def isEmpty(self):
        return self.top == None

    def pop(self):
        if self.isEmpty():
            raise Exception('Trying to pop from an empty stack')
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.isEmpty():
            raise Exception('Trying to peek from an empty stack')
        return self.top.value

