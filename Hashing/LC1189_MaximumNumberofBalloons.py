"""
Problem: 1189. Maximum Number of Balloons
Difficulty: Easy
Pattern: Hash Map / Frequency Counting

Description
Given a string text, return the maximum number of instances of the word
"balloon" that can be formed using the characters in text.

Each character in text can be used at most once.

Example:
Input:  text = "nlaebolko"
Output: 1

Input:  text = "loonbalxballpoon"
Output: 2

Approach
1. Count the frequency of each character in the string.
2. For the word "balloon":
   - 'b' → 1 time
   - 'a' → 1 time
   - 'l' → 2 times
   - 'o' → 2 times
   - 'n' → 1 time
3. Compute how many times we can form "balloon" using available characters.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        freq = {}

        # Count frequency of characters
        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        # Calculate maximum number of "balloon"
        return min(
            freq.get('b', 0),
            freq.get('a', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        )