"""
Problem: 14. Longest Common Prefix
Difficulty: Easy
Pattern: String / Vertical Scanning

Description
Write a function to find the longest common prefix string
among an array of strings.

If there is no common prefix, return an empty string "".

Example:
Input:  strs = ["flower","flow","flight"]
Output: "fl"

Input:  strs = ["dog","racecar","car"]
Output: ""

Approach (Vertical Scanning)
1. Take the first string as reference.
2. Compare each character index with all other strings.
3. If mismatch or index out of range → return result.
4. Otherwise, keep building prefix.

Time Complexity: O(n * m)
    n = number of strings
    m = length of smallest string

Space Complexity: O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        result = ""

        for i in range(len(strs[0])):

            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return result

            result += strs[0][i]

        return result