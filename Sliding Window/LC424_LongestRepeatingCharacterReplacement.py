"""
Problem: 424. Longest Repeating Character Replacement
Difficulty: Medium
Pattern: Sliding Window / Hash Map

Description
You are given a string s and an integer k.

You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
after performing at most k replacements.

Example:
Input:  s = "ABAB", k = 2
Output: 4

Input:  s = "AABABBA", k = 1
Output: 4

Approach
1. Use sliding window with two pointers (left, right).
2. Maintain a frequency map of characters in the current window.
3. Track the count of the most frequent character (max_freq).
4. If window size - max_freq > k:
   → shrink window from left
5. Keep updating the maximum window size.

Key Idea:
Window size - most frequent character count ≤ k

Time Complexity: O(n)
Space Complexity: O(1) (only 26 uppercase letters)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):

            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update max frequency in window
            max_freq = max(max_freq, freq[s[right]])

            # If invalid window, shrink from left
            if (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update result
            result = max(result, right - left + 1)

        return result