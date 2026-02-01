# LeetCode 643 - Maximum Average Subarray I
# Pattern: Sliding Window (Fixed Size)
#
# Problem:
#   Given an integer array nums and an integer k,
#   find the contiguous subarray of length k that has
#   the maximum average value and return this value.
#
# Approach:
#   Use a fixed-size sliding window:
#     1. Compute the sum of the first k elements.
#     2. Slide the window one step at a time:
#         - subtract the element leaving the window
#         - add the new element entering the window
#     3. Track the maximum window sum during the process.
#     4. Divide the maximum sum by k to get the maximum average.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Compute initial window sum
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]

        max_sum = curr_sum

        # Slide the window
        j = k
        while j < len(nums):
            curr_sum = curr_sum - nums[j - k] + nums[j]
            max_sum = max(max_sum, curr_sum)
            j += 1

        return max_sum / k
