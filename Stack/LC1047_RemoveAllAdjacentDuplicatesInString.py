"""
Problem: 1047. Remove All Adjacent Duplicates In String
Difficulty: Easy
Pattern: Stack

Description
You are given a string s consisting of lowercase English letters.

A duplicate removal consists of choosing two adjacent and equal letters
and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals.

Example
Input: s = "abbaca"
Output: "ca"

Explanation:
abbaca
-> aaca  (remove "bb")
-> ca    (remove "aa")

Approach
Use a stack.

1. Traverse the string.
2. If stack is empty OR current character != stack top → push.
3. If current character == stack top → pop (remove duplicate pair).
4. Join stack at the end to form the result string.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for ch in s:

            if not stack or ch != stack[-1]:
                stack.append(ch)
            else:
                stack.pop()

        return "".join(stack)