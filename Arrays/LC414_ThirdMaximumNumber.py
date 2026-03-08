# LC414 - Third Maximum Number
# LeetCode 414 | Easy
# Pattern: Array / Set


"""
Third Maximum Number

Given an integer array nums, return the third distinct maximum number.
If the third maximum does not exist, return the maximum number.

Approach:
- Remove duplicates using a set.
- If fewer than 3 unique numbers exist → return max.
- Otherwise return the third largest.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = set(nums)

        if len(nums) < 3:
            return max(nums)

        nums.remove(max(nums))
        nums.remove(max(nums))

        return max(nums)