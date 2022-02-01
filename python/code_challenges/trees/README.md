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
All Method will require a binarytree to be input

def add: takes a value then it will set a base case for if the the value is less than the current root.value which is if root.left is currently none then set the root.left to the new node with the current value. Else you will walk the root.left Same thing will be done on the else statement for the right side

def contains: will take in a value then will walk through the root then if root is none return false to say the value isn't there then check if the root.value is equal to the value if so return true indicating it is there otherwise check if the value is less than the root if so you will the walk of the root.left last we will check for any other condition which would be greater than and use that to return the walk on the right side. 

# Credits:
Brandon, Eddie, Connor, Isaiah, Michael, Roger, GeekForGeeks
