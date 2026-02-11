# LeetCode 704 - Binary Search
# Pattern: Binary Search
#
# Problem:
#   Given an array of integers nums which is sorted in ascending order,
#   and an integer target, write a function to search target in nums.
#   If target exists, return its index. Otherwise, return -1.
#
# Approach:
#   Use binary search:
#     - Initialize two pointers: low and high.
#     - Repeatedly compute the middle index.
#     - If nums[mid] equals target, return mid.
#     - If nums[mid] is smaller than target, search in the right half.
#     - If nums[mid] is greater than target, search in the left half.
#   Continue until low > high.
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
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
