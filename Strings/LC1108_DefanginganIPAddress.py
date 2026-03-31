"""
Problem: 1108. Defanging an IP Address
Difficulty: Easy
Pattern: String Manipulation

Description
Given a valid IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example:
Input:  address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input:  address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Approach
1. Traverse each character in the string.
2. If the character is ".", replace it with "[.]".
3. Otherwise, keep the character as it is.
4. Build the result using a list and join at the end.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:

        result = []

        for ch in address:
            if ch == ".":
                result.append("[.]")
            else:
                result.append(ch)

        return "".join(result)