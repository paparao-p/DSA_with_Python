# LC724 - Find Pivot Index
# LeetCode 724 | Easy
# Pattern: Prefix Sum (Running Sum)


"""
Find Pivot Index

Given an array of integers nums, calculate the pivot index.

The pivot index is the index where the sum of all numbers strictly
to the left of the index is equal to the sum of all numbers strictly
to the right of the index.

If no such index exists, return -1.
If there are multiple pivot indexes, return the leftmost one.

Approach:
- Compute total sum of array.
- Maintain a running left_sum.
- For each index i:
      right_sum = total_sum - left_sum - nums[i]
  If left_sum == right_sum → return i.
- Update left_sum as we move forward.

Time Complexity: O(n)
Space Complexity: O(1)
"""



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            
            if total_sum - left_sum - nums[i] == left_sum:
                return i
            
            left_sum += nums[i]

        return -1