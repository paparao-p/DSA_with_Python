# LeetCode 11 - Container With Most Water
# Pattern: Two Pointers
#
# Problem:
#   Given an array of non-negative integers height where each element
#   represents a vertical line at that position, find two lines that,
#   together with the x-axis, form a container that holds the most water.
#
# Approach:
#   Use two pointers:
#     - Left pointer starts at index 0.
#     - Right pointer starts at the last index.
#   At each step:
#     - Compute area = min(height[l], height[r]) * (r - l).
#     - Update maximum area.
#     - Move the pointer pointing to the shorter line inward,
#       because moving the taller line cannot increase the area.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxi = 0
        l = 0
        r = len(height) - 1

        while l < r:

            curr_area = min(height[l], height[r]) * (r - l)
            maxi = max(maxi, curr_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxi
