# LeetCode 69 - Sqrt(x)
# Pattern: Binary Search
#
# Problem:
#   Given a non-negative integer x, compute and return
#   the square root of x.
#   Since the return type is an integer, return the
#   floor value of the square root.
#
# Approach:
#   Use binary search between 0 and x//2 + 1:
#     - Compute mid.
#     - If mid * mid == x → return mid.
#     - If mid * mid < x → search right half.
#     - If mid * mid > x → search left half.
#   When the loop ends, high will be the floor of sqrt(x).
#
# Time Complexity: O(log x)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:

        low = 0
        high = x // 2 + 1

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1

        return high