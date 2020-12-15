# Stack with min element realization

### Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Task](#task)
* [Solution](#solution)

# General info
This code illustrates:
- Working stack with min element

# Technologies
- Python 3.9

# Task
Formally: implement a data structure that will handle queries of the following type:
- Insert X - add an element with the value X to the structure.
- Erase - delete the last added element (if the structure is empty, do nothing).
- Get - print the minimum value among all the elements that are currently in the structure (if the structure is empty, print the "Error" message).

# Solution
- The structure will be based on a stack, which already allows you to easily process all queries of the "Insert" and "Erase" types.
- We modify the standard implementation - in each cell of the stack we will store not only the value of the element itself, but also the minimum value among all elements that are "below" the current one in the stack.
- So when adding an element, we will need to save the number twice. Then check whether the stack was empty up to the current moment, and if it was not, then equate the minimum value for the added element to the minimum of itself and the minimum recorded in the next element.
- The delete operation has not changed in the implementation, except for deleting a pair of elements.
- The " Get " operation is now a check of the stack for emptiness, after which, if there is at least one element – you just need to output the minimum from the top of the stack.
