# Singly Linked List
<!-- Short summary or background information -->
We are making a linked list class that will then allow a user to add nodes with values to that list search if a value is in a node and then print out all of the node values

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

