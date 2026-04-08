"""
Problem: 1695. Maximum Erasure Value
Difficulty: Medium
Pattern: Sliding Window / Hash Set

Description
You are given an array of positive integers nums.

The goal is to select a subarray with unique elements and maximize the sum of its elements.

Return the maximum possible sum of such a subarray.

Example:
Input:  nums = [4,2,4,5,6]
Output: 17

Explanation:
The optimal subarray is [2,4,5,6] → sum = 17

Approach
1. Use a sliding window with two pointers (left, right).
2. Maintain a set to track unique elements.
3. If duplicate found:
   - Remove elements from left until duplicate is removed.
   - Update current sum accordingly.
4. Expand window and keep updating max sum.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        seen = set()
        left = 0
        curr_sum = 0
        result = 0

        for right in range(len(nums)):

            # Shrink window until no duplicate
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Expand window
            seen.add(nums[right])
            curr_sum += nums[right]

            result = max(result, curr_sum)

        return result