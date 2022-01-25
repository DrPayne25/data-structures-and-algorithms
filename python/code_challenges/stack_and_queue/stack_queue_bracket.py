from code_challenges.stack_and_queue.stack import Stack

def validateBrackets(string):
    stack = Stack()
    dictionary = {'{': '}', '(': ')', '[': ']'}
    for char in string:
        if char in '{[(':
            stack.push(char)
        elif char in '}])':
            if dictionary[stack.pop()] != char:
                return False
    if stack.isEmpty():
        return True
    else:
        return False
