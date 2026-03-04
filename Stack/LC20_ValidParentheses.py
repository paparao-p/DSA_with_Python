"""
LeetCode 20 - Valid Parentheses

Problem
Given a string s containing just the characters:
'(', ')', '{', '}', '[' and ']'

Determine if the input string is valid.

A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

Approach
Use a stack.

1. Push opening brackets into the stack.
2. When encountering a closing bracket:
   - Check if stack is empty → invalid
   - Check if top of stack matches the required opening bracket
3. If match → pop from stack
4. At the end, stack should be empty.

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