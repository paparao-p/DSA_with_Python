"""
Problem: 2351. First Letter to Appear Twice
Difficulty: Easy
Pattern: Hash Set

Description
Given a string s consisting of lowercase English letters,
return the first letter to appear twice.

Note:
- A letter appears twice when it is seen the second time.

Example:
Input:  s = "abccbaacz"
Output: "c"

Explanation:
The letter 'c' is the first to appear twice.

Approach
1. Use a set to track seen characters.
2. Traverse the string:
   - If character already exists in set → return it.
   - Else → add it to set.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:

        seen = set()

        for char in s:

            if char in seen:
                return char

            seen.add(char)