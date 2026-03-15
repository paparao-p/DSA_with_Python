"""
Problem: 448. Find All Numbers Disappeared in an Array
Difficulty: Easy
Pattern: Hash Map / Frequency Presence

Description
Given an array nums of size n where nums[i] is in the range [1, n],
return all the integers in the range [1, n] that do not appear in nums.

Example:
Input:  nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Explanation:
Numbers 5 and 6 are missing from the array.

Approach
1. Store all numbers from nums in a hashmap.
2. Traverse numbers from 1 to n.
3. If a number is not present in the hashmap, it means it is missing.
4. Add the missing numbers to the result list.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        mapping = {}

        for num in nums:
            mapping[num] = 1

        size = len(nums)
        result = []

        for num in range(1, size + 1):
            if num not in mapping:
                result.append(num)

        return result