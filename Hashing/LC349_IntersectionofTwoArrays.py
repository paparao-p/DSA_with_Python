"""
Problem: 349. Intersection of Two Arrays
Difficulty: Easy
Pattern: Hash Set / Set Intersection

Description
Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must be unique and you may return the result in any order.

Example:
Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Approach
1. Convert both arrays into sets to remove duplicates.
2. Use the set intersection operator (&) to find common elements.
3. Convert the result back to a list.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set(nums1) & set(nums2))


# Alternative Approach (Manual Hash Set)
#
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#
#         set1 = set(nums1)
#         result = set()
#
#         for num in nums2:
#             if num in set1:
#                 result.add(num)
#
#         return list(result)