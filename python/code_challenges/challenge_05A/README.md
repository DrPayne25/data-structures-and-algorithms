# Singly Linked List
<!-- Short summary or background information -->
We are making a linked list class that will then allow a user to add nodes with values to that list search if a value is in a node and then print out all of the node values it will also allow a user to add a new node to the end of the list insert a node before another node as well as insert a new node after another node.

## Challenge
<!-- Description of the challenge -->
not sure how this is different from the step up top

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O
time: 0(n)
space: log(n)

## API
<!-- Description of each method publicly available to your Linked List -->
insert will create a new node if none exist then make that the head. If a node exist it will add a new one but make that new node the new head and the existing one the next.

includes take a value and will search through the nodes while they have a value and if they match the inpputed value they will return a True otherwise it will return false

to_string will search through the nodes starting at the head and then take the current value of that node and using an f string will format it to a str that looks like this {value}

append will create a new node with the new value then see if the self.head has anything if not it will create a new node and then return it. Otherwise it will use a while loop to check through the list and until one of the nodes doesn't have a next value then add that new node to the end

insert_before will take a existing node and then insert a new node before it

insert after will take an existing node and then insert a new node after it.

## Whiteboards
Challenge 05: below one!
Challenge 06: ![challenge-06-WhiteBoard](code_challenges/Whiteboards/white_board_linked_list_insertions.jpg)


