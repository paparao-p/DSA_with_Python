"""
Problem: 75. Sort Colors
Difficulty: Medium
Pattern: Three Pointers (Dutch National Flag)

Description
Given an array nums with n objects colored red (0), white (1), and blue (2),
sort them in-place so that objects of the same color are adjacent.

Do not use built-in sort.

Example:
Input:  nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Approach
Use three pointers:
- low  → next position for 0
- mid  → current element
- high → next position for 2

Rules:
1. nums[mid] == 0 → swap with low, move both pointers
2. nums[mid] == 1 → move mid
3. nums[mid] == 2 → swap with high, move high only

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1