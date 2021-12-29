from code_challenges.challenge_05A.linked_list.linked_list import LinkedList, Node
import pytest

def test_node_instance():
    node = Node(1,None)
    assert node.next == None
    assert node.value == 1

def test_node_instance_failure():
    node = Node(1,None)
    assert node.next != node
    assert node.value != 2

def test_Linked_List():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_empty_linked_list():
    ll = LinkedList()
    assert ll.head == None

def test_insert_to_empty_linked_list():
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_insert_to_linked_list():
    ll = LinkedList()
    # head is empty or none
    node1 = Node('apple')
    # ll.head is none
    ll.head == node1
    # ll.head is apple
    node2 = Node('pear')
    #apple.next is none
    node1.next = node2
    # apple.next is pear
    # apple goes to pear which goes to none
    ll.insert('banana')
    # new order is banana to apple to pear
    assert ll.head.value == 'banana'

def test_includes_in_linked_list():
    ll = LinkedList()
    ll.insert('apple')
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    assert ll.includes('apple') == True

def test_includes_not_in_linked_list():
    ll = LinkedList()
    ll.insert('apple')
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    assert ll.includes('yellow') != True

def test_to_string_linked_list():
    ll = LinkedList()
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    assert ll.__str__() == "{ grape } -> { banana } -> { orange } -> None"

def test_to_string_not_working():
    ll = LinkedList()
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    assert ll.__str__() != "{ orange } -> { banana } -> { grape } -> None"

def test_append_single():
    ll = LinkedList()
    ll.insert('orange')
    ll.insert('banana')
    ll.append('grape')
    assert ll.__str__() == "{ banana } -> { orange } -> { grape } -> None"

def test_append_single_not_working():
    ll = LinkedList()
    ll.insert('orange')
    ll.insert('banana')
    ll.append('grape')
    assert ll.__str__() != "{ grape } -> { banana } -> { orange } -> None"

def test_append_multiple():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    assert ll.__str__() == "{ orange } -> { banana } -> { grape } -> None"

def test_append_multiple_not_working():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    assert ll.__str__() != "{ grape } -> { banana } -> { orange } -> None"

@pytest.mark.skip('Pending')
def test_insert_before_middle():
    ll = LinkedList()
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    ll.insert_before(2,"peach")
    assert ll.__str__() == "{ grape } -> { peach } -> { banana } { orange } -> None"

def test_insert_before_middle_not_working():
    ll = LinkedList()
    ll.insert('orange')
    ll.insert('banana')
    ll.insert('grape')
    ll.insert_before(2,"peach")
    assert ll.__str__() != "{ grape } -> { banana } -> { peach } { orange } -> None"

@pytest.mark.skip('Pending')
def test_insert_before_start():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    ll.insert_before(1,"peach")
    assert ll.__str__() == "{ peach } -> { grape } -> { banana } { orange } -> None"

def test_insert_before_start_not_working():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    ll.insert_before(1,"peach")
    assert ll.__str__() != "{ grape } -> { peach } -> { banana } { orange } -> None"

@pytest.mark.skip('Pending')
def test_insert_after_middle():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    ll.insert_after(1,"peach")
    assert ll.__str__() == "{ grape } -> { peach } -> { banana } { orange } -> None"

def test_kth_from_end_larger_than_list():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    assert ll.kth_from_end(4) == 'Exception'

def test_kth_from_end_same_size_list():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    assert ll.kth_from_end(2) == 'orange'

def test_kth_from_end_negative_integer():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    assert ll.kth_from_end(2) == 'Exception'

def test_kth_from_end_one():
    ll = LinkedList()
    ll.append('orange')
    assert ll.kth_from_end(0) == 'orange'

def test_kth_from_end_negative_integer():
    ll = LinkedList()
    ll.append('orange')
    ll.append('banana')
    ll.append('grape')
    assert ll.kth_from_end(1) == 'banana'









