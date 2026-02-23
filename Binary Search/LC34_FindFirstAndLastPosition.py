# LeetCode 34 - Find First and Last Position of Element in Sorted Array
# Pattern: Binary Search (Left Boundary + Right Boundary)
#
# Problem:
#   Given an array of integers nums sorted in non-decreasing order,
#   find the starting and ending position of a given target value.
#   If the target is not found in the array, return [-1, -1].
#
# Approach:
#   1. Use binary search to find the leftmost (first) occurrence of target.
#   2. If target is not found, return [-1, -1].
#   3. Use another binary search to find the rightmost (last) occurrence.
#   4. Return both indices.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        # Find Left Boundary
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        if nums[low] != target:
            return [-1, -1]

        left_index = low

        #  Find Right Boundary
        low = left_index
        high = len(nums) - 1

        while low < high:
            mid = (low + high + 1) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid - 1

        right_index = low

        return [left_index, right_index]