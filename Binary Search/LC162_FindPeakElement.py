# LeetCode 162 - Find Peak Element
# Pattern: Binary Search
#
# Problem:
#   A peak element is an element that is strictly greater
#   than its neighbors.
#   Given an integer array nums, return the index of any peak element.
#   You may assume nums[-1] = nums[n] = -∞.
#
# Approach:
#   Use binary search:
#     - Compare nums[mid] with nums[mid + 1].
#     - If nums[mid] < nums[mid + 1],
#         the peak lies on the right side.
#     - Otherwise,
#         the peak lies on the left side (including mid).
#   Continue until low == high.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low