# LeetCode 35 - Search Insert Position
# Pattern: Binary Search
#
# Problem:
#   Given a sorted array of distinct integers and a target value,
#   return the index if the target is found.
#   If not, return the index where it would be inserted
#   in order to maintain sorted order.
#
# Approach:
#   Use binary search:
#     - If nums[mid] == target → return mid.
#     - If nums[mid] > target → search left half.
#     - If nums[mid] < target → search right half.
#   If target is not found, the correct insert position
#   will be the value of `low` after the loop.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low
