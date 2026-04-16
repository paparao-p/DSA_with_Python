"""
Problem: 80. Remove Duplicates from Sorted Array II
Difficulty: Medium
Pattern: Two Pointers

Description
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element
appears at most twice.

Return the new length of the array.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place.

Example:
Input:  nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

Input:  nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]

Approach
1. Use two pointers:
   - left → position to place next valid element
   - right → iterate through array
2. Allow at most 2 duplicates:
   - Compare current element with nums[left - 2]
3. If different → place element at left pointer
4. Increment left pointer

Key Idea:
nums[right] != nums[left - 2]

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)

        left = 2  # position to place next valid element

        for right in range(2, len(nums)):

            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1

        return left