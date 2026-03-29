"""
Problem: 387. First Unique Character in a String
Difficulty: Easy
Pattern: Hash Map / Frequency Counting

Description
Given a string s, find the first non-repeating character in it
and return its index. If it does not exist, return -1.

Example:
Input:  s = "leetcode"
Output: 0

Input:  s = "loveleetcode"
Output: 2

Input:  s = "aabb"
Output: -1

Approach
1. Count the frequency of each character using a hashmap.
2. Traverse the string again:
   - Return the index of the first character with frequency = 1.
3. If no such character exists, return -1.

Time Complexity: O(n)
Space Complexity: O(1) (at most 26 lowercase letters)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        mapping = {}

        # Step 1: Count frequencies
        for char in s:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        # Step 2: Find first unique character
        for i in range(len(s)):
            if mapping[s[i]] == 1:
                return i

        return -1