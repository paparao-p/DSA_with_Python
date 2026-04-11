"""
Problem: 438. Find All Anagrams in a String
Difficulty: Medium
Pattern: Sliding Window / Frequency Count

Description
Given two strings s and p, return an array of all the start indices
of p's anagrams in s.

You may return the answer in any order.

Example:
Input:  s = "cbaebabacd", p = "abc"
Output: [0,6]

Explanation:
Substring "cba" at index 0 is an anagram of "abc"
Substring "bac" at index 6 is an anagram of "abc"

Approach
1. Use sliding window of size len(p).
2. Maintain frequency arrays for:
   - pattern (p_count)
   - current window (window)
3. Expand window by adding right character.
4. If window size exceeds len(p), remove left character.
5. Compare both frequency arrays:
   → If equal, it's an anagram → store index.

Time Complexity: O(n * 26) → effectively O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        result = []

        p_count = [0] * 26
        window = [0] * 26

        # Build frequency for pattern
        for char in p:
            p_count[ord(char) - ord('a')] += 1

        left = 0

        for right in range(len(s)):

            # Add current character to window
            window[ord(s[right]) - ord('a')] += 1

            # Maintain window size
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Compare frequency arrays
            if window == p_count:
                result.append(left)

        return result