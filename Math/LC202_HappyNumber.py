"""
Problem: 202. Happy Number
Difficulty: Easy
Pattern: Math + Hashing (Cycle Detection)

Description
Write an algorithm to determine if a number n is a happy number.

A happy number is defined as:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay),
  or it loops endlessly in a cycle.

Return True if n is a happy number, otherwise return False.

Example:
Input:  n = 19
Output: True

Explanation:
1² + 9² = 82  
8² + 2² = 68  
6² + 8² = 100  
1² + 0² + 0² = 1  → Happy Number
"""

class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1