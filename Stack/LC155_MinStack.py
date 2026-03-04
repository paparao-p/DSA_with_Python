"""
Problem: 155. Min Stack
Difficulty: Medium
Pattern: Stack / Design Data Structure

Description
Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

push(x)  -> Push element x onto stack
pop()    -> Removes the element on top of the stack
top()    -> Get the top element
getMin() -> Retrieve the minimum element in the stack

Approach
Use two stacks:

1. stack
   Stores all values.

2. minstack
   Stores the minimum value at each level.

When pushing:
Store min(previous_min, current_value).

The top of minstack always contains the current minimum.

Time Complexity
push   -> O(1)
pop    -> O(1)
top    -> O(1)
getMin -> O(1)

Space Complexity: O(n)
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]