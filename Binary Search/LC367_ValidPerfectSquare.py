"""
Problem: 367. Valid Perfect Square
Difficulty: Easy
Pattern: Binary Search / Math

Description
Given a positive integer num, return True if num is a perfect square,
otherwise return False.

A perfect square is an integer that is the square of another integer.

Example:
Input:  num = 16
Output: True

Input:  num = 14
Output: False

Note:
Do not use any built-in library function such as sqrt().

Approach
Use Binary Search.

1. Search numbers between 1 and num//2.
2. Compute mid * mid.
3. If mid * mid == num → perfect square.
4. If mid * mid > num → search left half.
5. If mid * mid < num → search right half.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        low = 1
        high = num // 2

        while low <= high:

            mid = (low + high) // 2
            val = mid * mid

            if val == num:
                return True

            elif val > num:
                high = mid - 1

            else:
                low = mid + 1

        return False