# LeetCode 125 - Valid Palindrome
# Pattern: Two Pointers / String Processing
#
# Problem:
#   Given a string s, determine if it is a palindrome,
#   considering only alphanumeric characters and ignoring cases.
#
# Approach:
#   Use two pointers:
#     - Left pointer starts from beginning.
#     - Right pointer starts from end.
#   Skip non-alphanumeric characters on both sides.
#   Compare lowercase characters.
#   If mismatch → return False.
#   If pointers cross → palindrome.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:

            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1          
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True