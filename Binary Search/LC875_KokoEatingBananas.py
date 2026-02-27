# LC875 - Koko Eating Bananas
# LeetCode 875 | Medium
# Pattern: Binary Search on Answer
#
# ------------------------------------------------------------
# Problem:
#   Koko loves bananas. There are piles of bananas, and she has h hours.
#   Each hour, she can eat at most k bananas from a single pile.
#   Return the minimum integer k such that she can finish all piles within h hours.
#
# ------------------------------------------------------------
# Approach:
#   Binary search the eating speed k:
#     - Minimum possible speed = 1
#     - Maximum possible speed = max(piles)
#   For each candidate speed (mid), compute total hours required.
#   If required hours > h → speed too slow → increase low.
#   Otherwise → try smaller speed → move high.
#
# ------------------------------------------------------------
# Time Complexity: O(n log max(piles))
# Space Complexity: O(1)
# ------------------------------------------------------------


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid  # ceil division

            if hours > h:
                low = mid + 1
            else:
                high = mid

        return low