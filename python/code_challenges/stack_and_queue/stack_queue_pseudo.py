from code_challenges.stack_and_queue.stack import Stack

class Pseudo_queue():
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
    def enqueue(self, value):
        self.stack_one.push(value)
    def dequeue(self):
        if self.stack_one.isEmpty() and self.stack_two.isEmpty():
            print('Trying to dequeue from an empty queue')
            return
        elif self.stack_two.size == 0 and self.stack_one.size > 0:
            while self.stack_one.size:
                temp = self.stack_one.pop()
                self.stack_two.push(temp)
            return self.stack_two.pop()
        else:
            return self.stack_two.pop()

if __name__ == '__main__':
    q = Pseudo_queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
