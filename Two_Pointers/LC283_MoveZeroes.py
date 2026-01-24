# LeetCode 283 - Move Zeroes
# Pattern: Two Pointers
#
# Problem:
#   Given an integer array nums, move all 0's to the end of it
#   while maintaining the relative order of the non-zero elements.
#   The operation must be done in-place.
#
# Approach:
#   Use two pointers:
#     - Pointer `l` tracks the position of a zero.
#     - Pointer `r` scans ahead for a non-zero element.
#   When nums[l] is zero and nums[r] is non-zero, swap them.
#   Otherwise, move pointers forward appropriately.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        l = 0
        r = 1

        while r < len(nums):

            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1

            elif nums[l] == 0 and nums[r] == 0:
                r += 1

            else:
                l += 1
                r += 1
