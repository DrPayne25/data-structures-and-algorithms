from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree, BinarySearchTree
from code_challenges.trees.tree_breadth_first import breadth_first

import pytest

def test_new_node():
    node = Node(11)
    actual = node.value
    expected = 11
    assert actual == expected

def test_new_node_bad():
    node = Node(11)
    actual = node.value
    expected = 12
    assert actual != expected

def test_bt_empty():
    bt = BinaryTree()
    assert bt

def test_bt_pre_order():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.pre_order()
    assert order_list == ['apple', 'pear', 'orange']

def test_bt_pre_order_not_working():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(pear)
    pear.left = orange
    pear.right = apple

    assert pear.left == bt.root.left
    assert pear.right == apple
    order_list = bt.pre_order()
    assert order_list != ['pear', 'apple', 'orange']

def test_bt_in_order():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(pear)
    pear.left = orange
    pear.right = apple

    assert pear.left == bt.root.left
    assert pear.right == apple
    order_list = bt.in_order()
    assert order_list == ['orange', 'pear', 'apple']

def test_bt_in_order_not_working():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(pear)
    pear.left = orange
    pear.right = apple

    assert pear.left == bt.root.left
    assert pear.right == apple
    order_list = bt.in_order()
    assert order_list != ['pear', 'orange', 'apple']

def test_bt_post_order():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(pear)
    pear.left = orange
    pear.right = apple

    assert pear.left == bt.root.left
    assert pear.right == apple
    order_list = bt.post_order()
    assert order_list == ['orange', 'apple', 'pear']

def test_bt_post_order():
    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(pear)
    pear.left = orange
    pear.right = apple

    assert pear.left == bt.root.left
    assert pear.right == apple
    order_list = bt.post_order()
    assert order_list == ['orange', 'apple', 'pear']

def test_bt_search_tree_left():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    actual = bt.pre_order()
    expected = ['orange', 'apple']
    assert actual == expected

def test_bt_search_tree_left_and_right():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    bt.add('pear')
    actual = bt.pre_order()
    expected = ['orange', 'apple', 'pear']
    assert actual == expected

def test_bt_search_tree_contains_true():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    bt.add('pear')
    bt.add('banana')
    actual = bt.contains('pear')
    expected = True
    assert actual == expected

def test_bt_search_tree_contains_false():
    root = Node('orange')
    bt = BinarySearchTree(root)
    bt.add('apple')
    bt.add('pear')
    bt.add('orange')
    actual = bt.contains('strawberry')
    expected = False
    assert actual == expected

def test_bt_search_tree_empty_false():
    bt = BinarySearchTree()
    actual = bt.contains('orange')
    expected = False
    assert actual == expected

def test_bt_max_value():
    one = Node(1)
    three = Node(3)
    four = Node(4)
    bt = BinaryTree(one)
    one.left = four
    one.right = three

    assert one.left == bt.root.left
    assert one.right == three
    max_value = bt.max_value()
    assert max_value == 4

def test_bt_max_value_not_working():
    seven = Node(7)
    nine = Node(9)
    twenty = Node(20)
    bt = BinaryTree(seven)
    seven.left = twenty
    seven.right = nine

    assert seven.left == bt.root.left
    assert seven.right == nine
    max_value = bt.max_value()
    assert max_value != 7

def test_bt_max_value_exception():
    with pytest.raises(Exception):
        bt = BinaryTree()
        bt.max_value()

def test_breadth_first():
    one = Node(1)
    three = Node(3)
    four = Node(4)
    bt = BinaryTree(one)
    one.left = four
    one.right = three

    assert one.left == bt.root.left
    assert one.right == three
    breadth = breadth_first(bt)
    assert breadth == [1,4,3]





