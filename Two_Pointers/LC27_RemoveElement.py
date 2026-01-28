# LeetCode 27 - Remove Element
# Pattern: Two Pointers
#
# Problem:
#   Given an integer array nums and an integer val,
#   remove all occurrences of val in-place.
#   The relative order of elements may be changed.
#   Return the number of elements remaining (k).
#   The first k elements of nums should contain the result.
#
# Approach:
#   Use two pointers:
#     - Left pointer `l` scans from the start.
#     - Right pointer `r` tracks the last valid position.
#   If nums[l] == val:
#       overwrite it with nums[r] and shrink right pointer.
#   Else:
#       move left pointer forward.
#   Since order doesn't matter, swapping from the back is allowed.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1

        return l
