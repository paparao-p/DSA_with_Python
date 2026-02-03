# LeetCode 485 - Max Consecutive Ones
# Pattern: Sliding Window / Two Pointers
#
# Problem:
#   Given a binary array nums, return the maximum number of
#   consecutive 1's in the array.
#
# Approach:
#   Use two pointers:
#     - `left` marks the start of the current streak of 1's.
#     - `right` scans through the array.
#   If nums[right] == 1:
#       update the maximum length using (right - left + 1).
#   If nums[right] == 0:
#       reset the window by moving left to right + 1.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_len = 0
        left = 0
        right = 0

        while right < len(nums):

            if nums[right] == 1:
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                right += 1
                left = right

        return max_len
