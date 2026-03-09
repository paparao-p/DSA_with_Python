"""
Problem: 242. Valid Anagram
Difficulty: Easy
Pattern: Hash Map / Frequency Counting

Description
Given two strings s and t, return True if t is an anagram of s,
otherwise return False.

An anagram is a word formed by rearranging the letters of another,
using exactly the same characters with the same frequency.

Example:
Input:  s = "anagram", t = "nagaram"
Output: True

Input:  s = "rat", t = "car"
Output: False

Approach
1. If lengths differ, they cannot be anagrams.
2. Use a hashmap to store character frequencies from string s.
3. Traverse string t:
   - If character not in hashmap → return False
   - Decrease its count
   - Remove it from hashmap when count becomes zero
4. If hashmap becomes empty, both strings had identical frequencies.

Time Complexity: O(n)
Space Complexity: O(1)   (at most 26 lowercase letters)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapping = {}

        for char in s:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        for char in t:
            if char not in mapping:
                return False

            mapping[char] -= 1

            if mapping[char] == 0:
                mapping.pop(char)

        return not mapping