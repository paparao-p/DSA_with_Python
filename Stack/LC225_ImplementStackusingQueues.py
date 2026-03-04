"""
Problem: 225. Implement Stack using Queues
Difficulty: Easy
Pattern: Stack Simulation / Queue Rotation

Description
Implement a Last-In-First-Out (LIFO) stack using only queues.

The implemented stack should support all the functions of a normal stack:

push(x)  -> Push element x onto stack
pop()    -> Removes the element on top of the stack
top()    -> Get the top element
empty()  -> Returns whether the stack is empty

Only standard operations of a queue are allowed:
- push to back
- pop from front
- size
- peek

Approach
Use a single queue and rotate elements after each push.

Steps:
1. Append the new element to the queue.
2. Rotate the previous elements by moving them from front to back.
3. This ensures the newest element stays at the front of the queue.

Example

push(1) → [1]
push(2) → [2,1]
push(3) → [3,2,1]

So pop() removes the most recent element, maintaining LIFO behavior.

Time Complexity
push  -> O(n)
pop   -> O(1)
top   -> O(1)
empty -> O(1)

Space Complexity: O(n)
"""

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:

        self.queue.append(x)

        # Rotate queue to move new element to the front
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()