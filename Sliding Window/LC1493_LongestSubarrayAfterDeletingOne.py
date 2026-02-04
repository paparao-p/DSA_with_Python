# LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
# Pattern: Sliding Window (At Most One Zero)
#
# Problem:
#   Given a binary array nums, delete exactly one element from the array.
#   Return the size of the longest non-empty subarray containing only 1's.
#
# Approach:
#   Use a sliding window with two pointers:
#     - Expand the right pointer.
#     - Count zeros inside the window.
#     - If zeros exceed 1, shrink the window from the left until
#       at most one zero remains.
#     - Track the maximum window length during the process.
#
#   Since exactly one element must be deleted, subtract 1 from the
#   final window size.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_len = 0
        left = 0
        zeroes = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        # Must delete exactly one element
        return max_len - 1
