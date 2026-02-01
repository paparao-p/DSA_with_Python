# LeetCode 3 - Longest Substring Without Repeating Characters
# Pattern: Sliding Window (Initial Version)
#
# Problem:
#   Given a string s, find the length of the longest substring
#   without repeating characters.
#
# Approach:
#   Use two pointers to represent a sliding window.
#   Expand the right pointer one step at a time.
#   When a duplicate character is found inside the window,
#   scan the window to move the left pointer just after
#   the previous occurrence.
#
# Note:
#   This initial version uses an inner scan inside the window,
#   so the worst-case time complexity is higher than optimal.
#   This will be optimized later using a hashmap-based approach.
#
# Time Complexity: O(n^2) in worst case
# Space Complexity: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)
        size = 0

        l = 0
        r = 1

        while r < length:

            if l == r:
                r += 1

            elif s[r] != s[l]:

                for i in range(l, r):
                    if s[i] == s[r]:
                        l = i + 1

                size = max(size, r - l + 1)
                r += 1

            else:
                l += 1

        if length == 0:
            return length
        elif size == 0:
            return 1
        else:
            return size
