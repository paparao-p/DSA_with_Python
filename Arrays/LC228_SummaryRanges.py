"""
Problem: 228. Summary Ranges
Difficulty: Easy
Pattern: Array Traversal / Two Pointers

Description
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
Each range should be represented as:

- "a->b" if a != b
- "a" if a == b

Example:
Input:  nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Input:  nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Approach
1. Track the start of a range.
2. Move through the array while numbers are consecutive.
3. When the sequence breaks, record the range.
4. Repeat until all numbers are processed.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []
        i = 0

        while i < len(nums):

            start = nums[i]

            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")

            i += 1

        return result