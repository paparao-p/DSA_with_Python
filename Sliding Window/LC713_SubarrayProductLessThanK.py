# LeetCode 713 - Subarray Product Less Than K
# Pattern: Sliding Window (Variable Size)
#
# Problem:
#   Given an array of positive integers nums and an integer k,
#   return the number of contiguous subarrays where the product
#   of all the elements in the subarray is strictly less than k.
#
# Approach:
#   Use a variable-size sliding window:
#     - Expand the right pointer and multiply the current element
#       into the window product.
#     - While the product is >= k, shrink the window from the left
#       by dividing out nums[left] and moving left forward.
#     - For every valid window ending at right, all subarrays
#       starting between left and right are valid, so add
#       (right - left + 1) to the count.
#   Special case:
#     - If k <= 1, no valid subarray exists (since all numbers are positive).
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0
        product = 1
        left = 0

        # Edge case: no valid subarray possible
        if k <= 1:
            return 0

        for right in range(len(nums)):

            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            count += (right - left + 1)

        return count
