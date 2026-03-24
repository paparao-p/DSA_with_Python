"""
Problem: 53. Maximum Subarray
Difficulty: Medium
Pattern: Kadane's Algorithm / Dynamic Programming

Description
Given an integer array nums, find the subarray with the largest sum,
and return its sum.

A subarray is a contiguous part of the array.

Example:
Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: Subarray [4,-1,2,1] has the largest sum = 6

Approach (Kadane's Algorithm)
1. Maintain a running sum (curr_sum).
2. At each step, decide:
   - Start a new subarray from current element
   - Or continue the previous subarray
3. Update the maximum result accordingly.

Formula:
curr_sum = max(nums[i], curr_sum + nums[i])
result   = max(result, curr_sum)

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            result = max(result, curr_sum)

        return result