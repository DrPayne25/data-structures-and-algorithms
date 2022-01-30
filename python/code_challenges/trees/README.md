# Trees
<!-- Short summary or background information -->
We are creating a Binary Tree with a Binary Search Tree subclass along with a new node class to handle the different ways it setup vs a stack and queue

## Challenge
<!-- Description of the challenge -->
Create a class to handle the new node a class to handle the BinaryTree and then a subclass for the BinarySearchTree

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O:
Time: O(n)
Space: O(1)

## API
<!-- Description of each method publicly available in each of your trees -->

## BinaryTree:

def pre_order: will walk through a binary tree and return the values in the order of root > left > right by appending the values at the root right away then walking through the left then right

def in_order: will walk through a binary tree and return the values in the order of left > root > right by walking through the root.left  then appending the values then walking through the root.right

def post_order: will walk through a binary tree and return the values in the order of left > right > root by walking through the root.left then the root.right then appending the values

## BinarySearchTree

def add: still working

def contains: still working

# Credits:
Brandon, Eddie, Connor, Isaiah, Michael, Roger, GeekForGeeks
