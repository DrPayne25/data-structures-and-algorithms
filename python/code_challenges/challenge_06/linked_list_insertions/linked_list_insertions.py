class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.net = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
