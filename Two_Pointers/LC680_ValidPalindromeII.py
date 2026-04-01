"""
Problem: 680. Valid Palindrome II
Difficulty: Easy
Pattern: Two Pointers / Greedy

Description
Given a string s, return True if the string can be a palindrome
after deleting at most one character.

Example:
Input:  s = "abca"
Output: True

Input:  s = "abc"
Output: False

Approach
1. Use two pointers (left, right).
2. If characters match → move both pointers inward.
3. If mismatch occurs:
   - Try skipping the left character OR
   - Try skipping the right character
4. If either case forms a palindrome → return True.

Helper function checks if a substring is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (
                    is_palindrome(left + 1, right) or
                    is_palindrome(left, right - 1)
                )

        return True