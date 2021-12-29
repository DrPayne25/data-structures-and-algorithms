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

    def __str__(self):
        try:
            current = self.head
            str_result = ''
            while current:
                str_result += f"{{ {current.value} }} -> "
                current = current.next
            return str_result + 'None'
        except Exception as e:
            print(f'The Follow error occurred {e}')

    def append(self, new_value):
        new_node = Node(new_value)
        current = self.head
        if current is None:
            self.head = new_node
            return

        while(current.next):
            current = current.next
        current.next = new_node

    def insert_before(self, next_value, new_value):
        if self.head.value == next_value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == next_value:
                    temp = current.next
                    current.next = Node(new_value, temp)
                    break
                current = current.next

    def insert_after(self, previous_node, new_value):
        pass

    def kth_from_end(self, k):
        temp = self.head #temp variable for head
        length = 0

        while temp is not None:
            temp = temp.next
            length += 1

        if k > length:
            return('Exception')

        temp = self.head
        for _ in range(1, length - k):
            temp = temp.next
        return(temp.value)


