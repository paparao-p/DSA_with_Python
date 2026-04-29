"""
Problem: 1662. Check If Two String Arrays are Equivalent
Difficulty: Easy
Pattern: Two Pointers / String Traversal

Description
Given two string arrays word1 and word2, return True if the two arrays
represent the same string, and False otherwise.

A string is represented by concatenating all elements in the array.

Example:
Input:  word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: True

Input:  word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: False

Approach (Optimized - No Join)
1. Use four pointers:
   - i, j → index of word arrays
   - x, y → index inside each string
2. Compare characters one by one.
3. Move pointers accordingly.
4. If mismatch → return False.
5. Ensure both arrays are fully traversed.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        i = j = 0      # pointers for word arrays
        x = y = 0      # pointers inside each string

        while i < len(word1) and j < len(word2):

            # Compare characters
            if word1[i][x] != word2[j][y]:
                return False

            x += 1
            y += 1

            # Move to next string in word1
            if x == len(word1[i]):
                i += 1
                x = 0

            # Move to next string in word2
            if y == len(word2[j]):
                j += 1
                y = 0

        # Both arrays should be fully traversed
        return i == len(word1) and j == len(word2)