"""
Problem: 350. Intersection of Two Arrays II
Difficulty: Easy
Pattern: Hash Map / Frequency Counting

Description
Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result should appear as many times as it appears
in both arrays. The result can be returned in any order.

Example:
Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Approach
1. Use a hashmap to store the frequency of elements in nums1.
2. Traverse nums2:
   - If the number exists in the hashmap, append it to result.
   - Decrease its frequency.
   - Remove it from the hashmap when the frequency becomes zero.

This ensures duplicates are counted correctly.

Time Complexity: O(n + m)
Space Complexity: O(min(n, m))
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = {}

        for num in nums1:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        result = []

        for num in nums2:
            if num in mapping:
                mapping[num] -= 1
                result.append(num)

                if mapping[num] == 0:
                    mapping.pop(num)

        return result