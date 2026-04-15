"""
Problem: 905. Sort Array By Parity
Difficulty: Easy
Pattern: Two Pointers / Partition

Description
Given an integer array nums, move all even integers to the beginning
of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example:
Input:  nums = [3,1,2,4]
Output: [2,4,3,1]  (order may vary)

Approach
1. Use two pointers:
   - left → position to place next even number
   - right → current element
2. Traverse the array:
   - If current element is even → swap with left pointer
   - Move left pointer forward
3. Continue until end of array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        left = 0

        for right in range(len(nums)):

            # Check if even using bit operation
            if nums[right] & 1 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums