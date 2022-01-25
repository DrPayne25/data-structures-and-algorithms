from code_challenges.stack_and_queue import queues
from code_challenges.stack_and_queue.node import Node
from code_challenges.stack_and_queue.queues import Queue
from code_challenges.stack_and_queue.stack import Stack
from code_challenges.stack_and_queue.stack_queue_pseudo import Pseudo_queue
from  code_challenges.stack_and_queue.stack_queue_animal_shelter import AnimalShelter
from  code_challenges.stack_and_queue.stack_queue_bracket import validateBrackets

import pytest

def test_node_instance():
    node = Node(1,None)
    assert node.next == None
    assert node.value == 1

#Test One Push onto a stack
def test_stack_push_one():
    stack = Stack()
    stack.push('1')
    assert stack.top.value == '1'

def test_stack_push_one_wrong():
    stack = Stack()
    stack.push('2')
    assert stack.top.value != '3'
#Test 2 Push multiple values onto a stack
def test_stack_push_multiple():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    assert stack.top.value == '6'

def test_stack_push_multiple_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    assert stack.top.value != '2'
#Test 3 pop off stack
def test_stack_pop_one():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    assert stack.top.value == '4'

def test_stack_pop_one_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    assert stack.top.value != '6'
#Test 4 empty a stack after multiple pops
def test_stack_pop_all():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top == None

def test_stack_pop_all_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top != '6'

#Test 5 Peek the next item on a stack
def test_peek_stack():
    stack = Stack()
    stack.push('2')
    assert stack.peek() == '2'

# @pytest.mark.skip('Pending')
def test_peek_stack_not_working():
    stack = Stack()
    stack.push('2')
    assert stack.peek() != '3'

#Test 6 instantiate an empty stack
def test_empty_stack():
    stack = Stack()
    actual = stack.isEmpty()
    expected = True
    assert actual == expected

def test_empty_stack_not_working():
    stack = Stack()
    stack.push('2')
    actual = stack.isEmpty()
    expected = True
    assert actual != expected

#Test 7 Calling pop or peek on empty stack raises exception
def test_peek_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()

def test_pop_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()

#Test 8 Enqueue one into a queue
def test_enqueue():
    queue = Queue()
    queue.enqueue('1')
    actual = queue.rear.value
    expected = ('1')
    assert actual == expected

def test_enqueue_not_working():
    queue = Queue()
    queue.enqueue('1')
    actual = queue.rear.value
    expected = ('2')
    assert actual != expected

#Test 9 Enqueue multiple into a queue
def test_enqueue():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    actual = queue.rear.value
    expected = ('4')
    assert actual == expected

def test_enqueue_front():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    actual = queue.front.value
    expected = ('1')
    assert actual == expected

def test_enqueue_not_working():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    actual = queue.rear.value
    expected = ('1')
    assert actual != expected

def test_enqueue_front_not_working():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    actual = queue.front.value
    expected = ('4')
    assert actual != expected

#Test 10 Dequeue out of a queue
def test_dequeue():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    queue.dequeue()
    actual = queue.front.value
    expected = ('2')
    assert actual == expected

def test_dequeue_not_working():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    queue.dequeue()
    actual = queue.front.value
    expected = ('1')
    assert actual != expected

#Test 11 peek into a queue
def test_peek_queue():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    actual = queue.peek()
    expected = ('1')
    assert actual == expected

def test_peek_queue_not_working():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    actual = queue.peek()
    expected = ('2')
    assert actual != expected

#Test 12 empty a queue after multiple dequeues
def empty_queue():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.dequeue()
    queue.dequeue()
    actual = queue.isEmpty()
    expected = (True)
    assert actual == expected

def empty_queue_not_working():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.dequeue()
    actual = queue.isEmpty()
    expected = (False)
    assert actual == expected

#Test 13 instantiate an empty queue
def test_empty_stack():
    queue = Queue()
    actual = queue.isEmpty()
    expected = True
    assert actual == expected

def test_empty_stack():
    queue = Queue()
    queue.enqueue('1')
    actual = queue.isEmpty()
    expected = False
    assert actual == expected

#Test 14 peek or dequeue raises exception

def test_peek_exception_queue():
    with pytest.raises(Exception):
        queue = Queue()
        queue.peek()

def test_dequeue_exception_queue():
    with pytest.raises(Exception):
        queue = Queue()
        queue.dequeue()

#Test 15 Pseudo Queue Enqueue
def test_pseudo_queue_enqueue():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.stack_one.size
    expected = (3)
    assert actual == expected

def test_pseudo_queue_enqueue_not_working():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.stack_one.size
    expected = (2)
    assert actual != expected

#Test 16 Pseudo Queue Dequeue

def test_pseudo_queue_dequeue_once():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.dequeue()
    expected = (1)
    assert actual == expected

def test_pseudo_queue_dequeue_multiple():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    actual = queue.dequeue()
    expected = (2)
    assert actual == expected

def test_pseudo_queue_dequeue_multiple_not_working():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    actual = queue.dequeue()
    expected = (1)
    assert actual != expected

def test_animal_shelter():
    animal_shelter = AnimalShelter()
    assert animal_shelter

def test_animal_shelter_enqueue_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('cat')
    actual = animal_shelter.in_stack.peek()
    expected = 'cat'
    assert actual == expected

def test_animal_shelter_enqueue_dog():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    actual = animal_shelter.in_stack.peek()
    expected = 'dog'
    assert actual == expected

def test_animal_shelter_enqueue_multiple():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('cat')
    actual = animal_shelter.in_stack.peek()
    expected = 'dog'
    assert actual == expected

def test_animal_shelter_enqueue_return_none():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    actual = animal_shelter.in_stack.peek()
    expected = 'cat'
    assert actual != expected

@pytest.mark.skip('Pending')
def test_animal_shelter_dequeue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('cat')
    animal_shelter.enqueue('cat')
    actual = animal_shelter.dequeue('cat')
    expected = 'cat'
    assert actual == expected

def test_matching_working():
    string = '{}'
    actual = validateBrackets(string)
    expected = True
    assert actual == expected

def test_matching_working2():
    string = '[{abc}]'
    actual = validateBrackets(string)
    expected = True
    assert actual == expected

def test_matching_working3():
    string = '(acb[{bb}])'
    actual = validateBrackets(string)
    expected = True
    assert actual == expected

def test_matching_working4():
    string = '()'
    actual = validateBrackets(string)
    expected = True
    assert actual == expected



