# LeetCode 209 - Minimum Size Subarray Sum
# Pattern: Sliding Window (Variable Size)
#
# Problem:
#   Given an array of positive integers nums and a positive integer target,
#   return the minimal length of a contiguous subarray of which the sum
#   is greater than or equal to target.
#   If there is no such subarray, return 0 instead.
#
# Approach:
#   Use a variable-size sliding window:
#     - Expand the right pointer to increase the window sum.
#     - When the window sum becomes >= target, try shrinking
#       the window from the left to minimize its size.
#     - Track the minimum window length during the process.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_arr = 999999
        total = 0
        l = 0

        for r in range(len(nums)):

            total += nums[r]

            while total >= target:
                min_arr = min(min_arr, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if min_arr == 999999 else min_arr
