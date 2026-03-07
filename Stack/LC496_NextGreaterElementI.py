"""
Problem: 496. Next Greater Element I
Difficulty: Easy
Pattern: Monotonic Stack

Description
You are given two arrays nums1 and nums2 where nums1 is a subset of nums2.

For each element in nums1, find the next greater element in nums2.
The next greater element of a number x in nums2 is the first greater
number to its right in nums2.

If no such element exists, return -1.

Approach
1. Use a monotonic decreasing stack to process nums2.
2. The stack stores indices of elements waiting to find their next greater.
3. When a larger element appears, pop smaller elements and record their
   next greater value.
4. Store results in an array corresponding to nums2.
5. Use a hashmap to map each number in nums2 to its index.
6. Build the answer for nums1 using this mapping.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        result = [-1] * len(nums2)
        mapping = {}

        for i in range(len(nums2)):

            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                result[index] = nums2[i]

            stack.append(i)
            mapping[nums2[i]] = i

        return [result[mapping[num]] for num in nums1]