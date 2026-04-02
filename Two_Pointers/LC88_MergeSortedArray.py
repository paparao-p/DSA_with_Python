"""
Problem: 88. Merge Sorted Array
Difficulty: Easy
Pattern: Two Pointers (Reverse) / In-place Merge

Description
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n representing the number of elements in nums1 and nums2 respectively.

Merge nums2 into nums1 as one sorted array in-place.

The final sorted array should not be returned, but instead be stored inside nums1.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output:
[1,2,2,3,5,6]

Approach (Reverse Two Pointers)
1. Start from the end of both arrays:
   - i → last valid element in nums1 (m - 1)
   - j → last element in nums2 (n - 1)
   - k → last index of nums1 (m + n - 1)

2. Compare nums1[i] and nums2[j]:
   - Place the larger value at nums1[k]
   - Move the corresponding pointer

3. If nums2 still has elements, copy them to nums1

Why reverse?
→ Avoid overwriting elements in nums1

Time Complexity: O(m + n)
Space Complexity: O(1)
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1