"""
Problem: 20. Valid Parentheses
Difficulty: Easy
Pattern: Stack

Description
Given a string s containing just the characters:
'(', ')', '{', '}', '[' and ']'

Determine if the input string is valid.

A string is valid if:
1. Open brackets must be closed by the same type.
2. Open brackets must be closed in correct order.
3. Every closing bracket has a corresponding opening bracket.

Approach
Use a stack to track opening brackets.

1. Push opening brackets to stack
2. When encountering closing bracket:
   - Check if stack is empty
   - Check if top matches expected opening bracket
3. If valid → pop
4. At end stack must be empty

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:

            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack