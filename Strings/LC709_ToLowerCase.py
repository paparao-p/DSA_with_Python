"""
Problem: 709. To Lower Case
Difficulty: Easy
Pattern: String Manipulation / ASCII Conversion

Description
Given a string s, return the string after replacing every uppercase letter
with the same lowercase letter.

Example:
Input:  s = "Hello"
Output: "hello"

Input:  s = "LOVELY"
Output: "lovely"

Approach
1. Traverse each character in the string.
2. If the character is uppercase ('A' to 'Z'):
   - Convert it to lowercase using ASCII difference.
3. Otherwise, keep it unchanged.
4. Build the result using a list and join at the end.

ASCII Insight:
- Difference between uppercase and lowercase letters = 32
- chr(ord(ch) + 32) converts uppercase → lowercase

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def toLowerCase(self, s: str) -> str:

        result = []

        for ch in s:

            if "A" <= ch <= "Z":
                result.append(chr(ord(ch) + 32))
            else:
                result.append(ch)

        return "".join(result)