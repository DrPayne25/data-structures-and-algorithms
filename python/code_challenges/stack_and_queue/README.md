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

def push: will create a new node then set the next node to the current top the set the new top to the new node

def isEmpty: will return a boolean of true if the stack is empty and false if it is not

def pop: will handle an empty stack by raising an exception. it will then create a temp variable set to the top then set the current top to the next then set the temp next to none and return the temp value

def peek: will handle an empty stack by raising an exception. It will then return the current top value

Queue

def isEmpty: will return a boolean of true if the queue is empty and false if it is not

def enqueue: will create a new node with the given value then if the queue is empty set the front and rear to the new node. If it's not empty it will set the self.rear.next to the new node along with the rear

def enqueue: will raise and exception on an empty queue. it will then create a temp variable set to the front set the front to the temp varible next then set the temp next to none and finally return the temp value

def peek: will handle an empty queue by raising an exception. It will then return the current front value

Credit:
Brandon, Eddie, Connor, Kassie, Roger, Ed, GeekForGeeks

# 
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

def push: will create a new node then set the next node to the current top the set the new top to the new node

def isEmpty: will return a boolean of true if the stack is empty and false if it is not

def pop: will handle an empty stack by raising an exception. it will then create a temp variable set to the top then set the current top to the next then set the temp next to none and return the temp value

def peek: will handle an empty stack by raising an exception. It will then return the current top value

Queue

def isEmpty: will return a boolean of true if the queue is empty and false if it is not

def enqueue: will create a new node with the given value then if the queue is empty set the front and rear to the new node. If it's not empty it will set the self.rear.next to the new node along with the rear

def enqueue: will raise and exception on an empty queue. it will then create a temp variable set to the front set the front to the temp varible next then set the temp next to none and finally return the temp value

def peek: will handle an empty queue by raising an exception. It will then return the current front value

Credit:
Brandon, Eddie, Connor, Kassie, Roger, Ed, GeekForGeeks
