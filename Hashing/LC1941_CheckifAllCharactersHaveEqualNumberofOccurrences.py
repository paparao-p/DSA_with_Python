"""
Problem: 1941. Check if All Characters Have Equal Number of Occurrences
Difficulty: Easy
Pattern: Hash Map / Set

Description
Given a string s, return True if all characters in s have the same
number of occurrences, otherwise return False.

Example:
Input:  s = "abacbc"
Output: True
Explanation: All characters appear 2 times

Input:  s = "aaabb"
Output: False

Approach
1. Count the frequency of each character using a hashmap.
2. Convert the frequency values into a set.
3. If all frequencies are equal → set size will be 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        mapping = {}

        # Count frequency of characters
        for char in s:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        # Check if all frequencies are equal
        return len(set(mapping.values())) == 1