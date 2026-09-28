"""
Problem: 1614. Maximum Nesting Depth of the Parentheses
Difficulty: Easy
Pattern: String Traversal / Counter

Description
Given a valid parentheses string s, return the maximum nesting depth
of the parentheses.

The nesting depth is the maximum number of nested parentheses at any
point in the string.

Example:
Input:  s = "(1+(2*3)+((8)/4))+1"
Output: 3

Input:  s = "(1)+((2))+(((3)))"
Output: 3

Approach
1. Use a counter to track the current nesting depth.
2. When '(' is encountered:
   - Increase the counter.
   - Update the maximum depth.
3. When ')' is encountered:
   - Decrease the counter.
4. Return the maximum depth found.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxDepth(self, s: str) -> int:

        count = 0
        max_depth = 0

        for char in s:

            if char == "(":
                count += 1
                max_depth = max(max_depth, count)

            elif char == ")":
                count -= 1

        return max_depth