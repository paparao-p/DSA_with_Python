# LeetCode 153 - Find Minimum in Rotated Sorted Array
# Pattern: Binary Search (Rotated Array)
#
# Problem:
#   Suppose an array of length n sorted in ascending order
#   is rotated between 1 and n times.
#   Given the sorted rotated array nums (without duplicates),
#   return the minimum element.
#
# Approach:
#   Use binary search:
#     - Compare nums[mid] with nums[high].
#     - If nums[mid] > nums[high], the minimum lies in the right half.
#     - Otherwise, the minimum lies in the left half (including mid).
#   Continue until low == high.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]