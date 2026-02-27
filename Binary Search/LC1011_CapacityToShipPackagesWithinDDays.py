# ============================================================
# LC1011 - Capacity To Ship Packages Within D Days
# LeetCode 1011 | Medium
# Pattern: Binary Search on Answer
# ============================================================

"""
Problem:
Given an array weights where weights[i] is the weight of the i-th package,
and an integer days representing the number of days to ship all packages,
return the least weight capacity of the ship so that all packages can be
shipped within the given days.

Approach:
- Minimum possible capacity = max(weights)
  (Ship must carry at least the heaviest package.)
- Maximum possible capacity = sum(weights)
  (Ship everything in one day.)

Binary search on this capacity range:
For each candidate capacity:
    - Simulate loading packages in order.
    - Count how many days are required.
If required days > given days:
    → capacity too small → increase low.
Else:
    → try smaller capacity → move high.

Time Complexity: O(n log(sum(weights)))
Space Complexity: O(1)
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            required_days = 1
            current_weight = 0

            for w in weights:
                if current_weight + w <= mid:
                    current_weight += w
                else:
                    required_days += 1
                    current_weight = w

            if required_days > days:
                low = mid + 1
            else:
                high = mid

        return low