# LeetCode 33 - Search in Rotated Sorted Array
# Pattern: Modified Binary Search
#
# Problem:
#   There is an integer array nums sorted in ascending order,
#   but it may be rotated at some pivot.
#   Given the array and a target value, return its index
#   if found, otherwise return -1.
#
# Approach:
#   Use modified binary search:
#     - Find mid.
#     - One half (left or right) must always be sorted.
#     - Determine which half is sorted.
#     - Check if target lies inside the sorted half.
#     - Narrow search accordingly.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1