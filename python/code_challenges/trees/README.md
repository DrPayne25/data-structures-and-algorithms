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

# Tree Max
<!-- Short summary or background information -->
we are creating a new method on the binary tree class that will find the max value in a binary tree

## Challenge
<!-- Description of the challenge -->
create a method called max_value that will ge the max value in a binary tree

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O:
Time: O(n)
Space: O(1)

## API
<!-- Description of each method publicly available in each of your trees -->

## BinaryTree:

def max_value: will take it self then throw and exception if the tree is empty then it will create a variable called z that will be dictionary with the key of max_value with a current value of 0 then we follow our previous post_order walk function but instead of appending the values we will check to see if the current node.value is greater than our z dictionary value if so then we will set the z dictionary value to the current node value and walk the rest of the nodes
then return the current z dictionary value

# Credits:
Brandon, Eddie, Connor, Michael, Roger, GeekForGeeks

# Tree Breadth First
<!-- Short summary or background information -->
we are creating a new module called tree_breadth_first which will take in a tree and then give a list of the values in the order they were encountered

## Challenge
<!-- Description of the challenge -->
create a function called breadth_first that will return a list of the values in the order they were encountered

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O:
Time: O(n)
Space: O(w) w = width of the tree

## API
<!-- Description of each method publicly available in each of your trees -->
breadth_first: takes a tree as an input then it will instantiate an empty list and a new queue then it will check if the tree.root is None if so it will return the list then it will enqueue the current tree.root into the queue the while the queue is not empty it will then have a new variable deqeueu set to the dequeue function for a queue which we will use to append all the values into our list created above  it will then do this for bot the left and right side of the list then finally return the list


# Credits:
Brandon, Eddie, Connor, Michael, Roger, GeekForGeeks

