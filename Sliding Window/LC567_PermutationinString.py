"""
Problem: 567. Permutation in String
Difficulty: Medium
Pattern: Sliding Window / Frequency Count

Description
Given two strings s1 and s2, return True if s2 contains a permutation of s1,
or False otherwise.

In other words, check if one of s1's permutations is a substring of s2.

Example:
Input:  s1 = "ab", s2 = "eidbaooo"
Output: True

Explanation:
Substring "ba" is a permutation of "ab"

Approach
1. If s1 is longer than s2 → return False.
2. Use fixed-size sliding window of size len(s1).
3. Maintain frequency arrays:
   - target → for s1
   - window → for current substring in s2
4. Expand window by adding right character.
5. If window size exceeds → remove left character.
6. Compare frequency arrays:
   → If equal → permutation found.

Time Complexity: O(n * 26) → effectively O(n)
Space Complexity: O(1)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        # Build frequency for s1
        for ch in s1:
            target[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):

            # Add current character to window
            window[ord(s2[right]) - ord('a')] += 1

            # Maintain window size
            if right - left + 1 > len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # Check if current window is a permutation
            if window == target:
                return True

        return False