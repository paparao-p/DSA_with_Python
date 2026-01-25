# LeetCode 26 - Remove Duplicates from Sorted Array
# Pattern: Two Pointers
#
# Problem:
#   Given a sorted integer array nums, remove the duplicates in-place
#   such that each unique element appears only once.
#   Return the number of unique elements (k).
#   The first k elements of nums should contain the result.
#
# Approach:
#   Use two pointers:
#     - Pointer `l` tracks the position of the last unique element.
#     - Pointer `r` scans the array.
#   If nums[l] == nums[r], move r forward.
#   If different, move l forward and overwrite nums[l] with nums[r].
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        l = 0
        r = 1

        while r < len(nums):

            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
                r += 1

        return l + 1
