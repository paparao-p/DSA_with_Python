# LC303 - Range Sum Query: Immutable
# LeetCode 303 | Easy
# Pattern: Prefix Sum


"""
Range Sum Query: Immutable

Given an integer array nums, handle multiple queries of the form:
    sumRange(left, right)
Return the sum of elements between indices left and right (inclusive).

Approach:
- Build a prefix sum array where:
      prefix[i] = sum of first i elements
- Then:
      sumRange(left, right) = prefix[right + 1] - prefix[left]

Time Complexity:
    Initialization → O(n)
    Each Query     → O(1)

Space Complexity:
    O(n)
"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]