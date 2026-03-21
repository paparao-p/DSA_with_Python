"""
Problem: 1544. Make The String Great
Difficulty: Easy
Pattern: Stack / String Processing

Description
Given a string s of lower and upper case English letters.

A good string is one where:
- No two adjacent characters are the same letter but in different cases.

Example:
'a' and 'A' are the same letter but different cases → remove them.

Keep removing such adjacent pairs until the string becomes good.

Return the final string.

Example:
Input:  s = "leEeetcode"
Output: "leetcode"

Input:  s = "abBAcC"
Output: ""

Approach
Use a stack:

1. Traverse each character in the string.
2. If stack is not empty and the current character and top of stack
   differ by 32 in ASCII → they are same letter with different cases.
3. Pop the stack.
4. Otherwise, push the character.
5. Join the stack to form the result.

ASCII Trick:
Difference between lowercase and uppercase letters = 32

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for char in s:

            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)