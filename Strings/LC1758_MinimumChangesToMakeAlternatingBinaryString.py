"""
Problem: 1758. Minimum Changes To Make Alternating Binary String
Difficulty: Easy
Pattern: String Greedy / Pattern Matching

Description
You are given a binary string s.

A string is alternating if no two adjacent characters are equal.

Example valid alternating strings:
"0101", "1010"

Return the minimum number of operations needed to make s alternating.

In one operation, you can change any '0' to '1' or '1' to '0'.

Approach
Only two valid alternating patterns exist:

1. Starting with '0' → 010101...
2. Starting with '1' → 101010...

We count how many changes are needed for both patterns and
return the minimum.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def minOperations(self, s: str) -> int:

        # Pattern starting with '0' → 010101...
        count1 = 0
        prev_digit = 0

        for digit in s:
            if prev_digit == int(digit):
                prev_digit = int(digit) ^ 1
                count1 += 1
            else:
                prev_digit = int(digit)

        # Pattern starting with '1' → 101010...
        count2 = 0
        prev_digit = 1

        for digit in s:
            if prev_digit == int(digit):
                prev_digit = int(digit) ^ 1
                count2 += 1
            else:
                prev_digit = int(digit)

        return min(count1, count2)