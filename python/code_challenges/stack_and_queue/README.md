# Stacks and Queues
<!-- Short summary or background information -->
We are making 3 separate classes one for a node, stack, and queue.

## Challenge
<!-- Description of the challenge -->
The node should create an empty node when called. Stack should create an empty stack with 3 methods of push, isEmpty, pop, and peek. Queue should create an empty queue and have 4 methods isEmpty, enqueue, dequeue, and peek
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O
Space: O(1)
Time: O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->

Stack

def push: will create a new node then set the next node to the current top the set the new top to the new node and will then add one to the self.size

def isEmpty: will return a boolean of true if the stack is empty and false if it is not

def pop: will handle an empty stack by raising an exception. it will then create a temp variable set to the top then set the current top to the next then set the temp next to none and return the temp value and will remove one for the self.size

def peek: will handle an empty stack by raising an exception. It will then return the current top value

def size: Will return the current value for self.size

Queue

def isEmpty: will return a boolean of true if the queue is empty and false if it is not

def enqueue: will create a new node with the given value then if the queue is empty set the front and rear to the new node. If it's not empty it will set the self.rear.next to the new node along with the rear

def enqueue: will raise and exception on an empty queue. it will then create a temp variable set to the front set the front to the temp varible next then set the temp next to none and finally return the temp value

def peek: will handle an empty queue by raising an exception. It will then return the current front value

Credit:
Brandon, Eddie, Connor, Kassie, Roger, Ed, GeekForGeeks

# Pseudo Queue
<!-- Short summary or background information -->
We are creating a queue using two stacks

## Challenge
<!-- Description of the challenge -->
Create a pseduo queue class that will use two stacks to create a queue like enqueue and dequeue methods
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O
Space: O(n)
Time: O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->

Pseudo Queue

enqueue: takes one argument will push the the argument into self.stack_one

dequeue: will return an error if the current stacks are empty then while self.stack two is empty and self.stack one has a value it will create a temp value with the current pop value from stack one it will then push that temp value into stack two and then return the pop of stack two


Credit:
Brandon, Eddie, Connor, Roger, Michael, [GeekForGeeks](https://www.geeksforgeeks.org/queue-using-stacks/)

# Animal Shelter
<!-- Short summary or background information -->
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.

## Challenge
<!-- Description of the challenge -->
Create a AnimalShelter class that will use two stacks to create a queue like enqueue and dequeue methods for a animal shelter
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O
Space: O(n)
Time: O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->

AnimalShelter

enqueue: takes one argument that if not equal to dog or cat will return none it will then push that animal into the top of stack one while giving the out stack the new value if needed

dequeue: will take one argument and if that argument is not equal to dog or cat return none if the argument is cat and the top value equals cat op that current top
the same applies to if the argument is dog


Credit:
Brandon, Eddie, Connor, Roger, [GeekForGeeks](https://www.geeksforgeeks.org/queue-using-stacks/)
