"""
Problem: 977. Squares of a Sorted Array
Difficulty: Easy
Pattern: Array Manipulation / Sorting

Description
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in
non-decreasing order.

Example:
Input:  nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Input:  nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Approach
1. Traverse the array and square each element.
2. Sort the array after squaring.
3. Return the sorted array.

Time Complexity: O(n log n)
Space Complexity: O(1) (in-place modification)
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        nums.sort()
        return nums