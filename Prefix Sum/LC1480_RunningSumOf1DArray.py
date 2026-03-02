# LC1480 - Running Sum of 1D Array
# LeetCode 1480 | Easy
# Pattern: Prefix Sum (In-place)


"""
Running Sum of 1D Array

Given an array nums, return the running sum of nums.

Running sum at index i:
    nums[0] + nums[1] + ... + nums[i]

Approach:
- Iterate from index 1 to end.
- Update each element as:
      nums[i] = nums[i] + nums[i-1]
- Modify the array in-place.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        return nums