"""
Problem: 844. Backspace String Compare
Difficulty: Easy
Pattern: Stack / String Simulation

Description
Given two strings s and t, return True if they are equal when both are typed
into empty text editors. '#' represents a backspace character.

Example:
Input:  s = "ab#c", t = "ad#c"
Output: True

Input:  s = "ab##", t = "c#d#"
Output: True

Approach
Simulate typing using a stack.

1. Traverse each string.
2. If the character is not '#', push it to the stack.
3. If the character is '#', pop from the stack (if not empty).
4. After processing both strings, compare the resulting stacks.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack_s = []

        for char in s:
            if char == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)

        stack_t = []

        for char in t:
            if char == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)

        return stack_s == stack_t