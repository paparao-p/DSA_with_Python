# LeetCode 344 - Reverse String
# Pattern: Two Pointers
#
# Problem:
#   Given an array of characters s, reverse the array in-place.
#   You must do this by modifying the input array with O(1) extra memory.
#
# Approach:
#   Use two pointers:
#     - Left pointer starts at index 0.
#     - Right pointer starts at the last index.
#   Swap characters at both pointers.
#   Move both pointers inward until they cross.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def reverseString(self, s: List[str]) -> None:

        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
