"""
Problem: 392. Is Subsequence
Difficulty: Easy
Pattern: Two Pointers

Description
Given two strings s and t, return True if s is a subsequence of t,
or False otherwise.

A subsequence is a string that can be derived from another string by
deleting some (or no) characters without changing the order of the
remaining characters.

Example:
Input:  s = "abc", t = "ahbgdc"
Output: True

Input:  s = "axc", t = "ahbgdc"
Output: False

Approach
1. Use two pointers:
   - i → pointer for string s
   - j → pointer for string t
2. Traverse t:
   - If characters match → move both pointers
   - Else → move pointer j only
3. If i reaches end of s → all characters matched

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)