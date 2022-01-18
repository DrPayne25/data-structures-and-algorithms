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

class Pseudo_queue():
    def __init__(self):
        self.stack_one = []
        self.stack_two = []
    def enqueue(self, value):
        self.stack_one.append(value)
    def dequeue(self):
        if len(self.stack_one) == 0 and len(self.stack_two) == 0:
            print('Trying to dequeue from an empty queue')
            return
        elif len(self.stack_two) == 0 and len(self.stack_one) > 0:
            while len(self.stack_one):
                temp = self.stack_one.pop()
                self.stack_two.append(temp)
            return self.stack_two.pop()
        else:
            return self.stack_two.pop()

        # if self.stack_two.isEmpty:
        #     while self.stack_one.size() > 0:
        #         self.stack_two.push(self.stack_one.pop())
        # return self.stack_two.top.pop()

        # if not self.stack_one.isEmpty():
        #     while self.stack_one.size()> 0:
        #         self.stack_two.push(self.stack_one.pop())
        #     res = self.stack_two.pop()
        #     while self.stack_two.size()> 0:
        #         self.stack_one.push(self.stack_two.pop())
        #     return res

if __name__ == '__main__':
    q = Pseudo_queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
