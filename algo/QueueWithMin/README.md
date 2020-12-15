# Queue with min element realization

### Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Task](#task)
* [Solution](#solution)

# General info
This code illustrates:
- Working queue with min element

# Technologies
- Python 3.9

# Task
Formally: implement a data structure that will handle queries of the following type:
- Insert X - add an element with the value X to the structure.
- erase - delete an element that was added earlier than all elements in the structure (if the structure is empty, do nothing).
- Get - print the minimum value among all the elements that are currently in the structure (if the structure is empty, print the "Error" message).

# Solution
- this task is a more complicated version of the same with stack, and the idea remains the same.
- the structure should now be based on a queue. then again, it is immediately clear that delete and add requests are not difficult.
- in order to solve the problem with the minimum request, you need to implement a queue using two stacks.
- the idea is that each element initially goes to stack1, then to stack2, and after that it can already be removed from the queue. that is, if we want to add an element to the queue, then we simply add it to the stack-trivially.
- If we want to delete an element, we will delete it from stack 2, but it may be empty. In this case, it is necessary to "pour" all the elements from stack 1 to stack 2, thereby obtaining the order of the queue-the First In First Out principle. This point raises the question of optimality, but is easily countered by the fact that each element will visit each of the two stacks no more than once, which means that no more than two operations are spent on each element in total.
- And finally, the minimum operation. But it is not more difficult than in the previous task. In our structure, we will use not just stacks, but the same stacks with a minimum, which means that the response to such a request will simply be the minimum of responses for each stack. It remains to carefully handle cases with empty stacks, which is easily done by checking two conditions.
