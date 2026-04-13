"""
Problem: 1768. Merge Strings Alternately
Difficulty: Easy
Pattern: Two Pointers / String Manipulation

Description
You are given two strings word1 and word2.

Merge the strings by adding letters in alternating order,
starting with word1.

If a string is longer than the other, append the remaining letters
to the end of the merged string.

Return the merged string.

Example:
Input:  word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input:  word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Input:  word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Approach
1. Use two pointers for both strings.
2. Append characters alternately.
3. After one string ends, append remaining characters.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged = []
        i, j = 0, 0

        # Alternate merging
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters
        return "".join(merged) + word1[i:] + word2[j:]