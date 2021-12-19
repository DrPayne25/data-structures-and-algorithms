class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        try:
            new_node = Node(value)
            # if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        except Exception as e:
            print(f'The Follow error occurred {e}')

    def includes(self, value):
        try:
            current = self.head
            # think of the below statement as while I have a current value in head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False
        except Exception as e:
            print(f'The Follow error occurred {e}')

    def to_string(self):
        try:
            current = self.head
            str_result = ''
            while current:
                str_result += f"{{ {current.value} }} -> "
                current = current.next
            return str_result + 'None'
        except Exception as e:
            print(f'The Follow error occurred {e}')



