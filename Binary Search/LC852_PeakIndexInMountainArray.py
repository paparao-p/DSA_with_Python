# LeetCode 852 - Peak Index in a Mountain Array
# Pattern: Binary Search (Mountain Array)
#
# Problem:
#   An array arr is a mountain array if:
#     - arr.length >= 3
#     - There exists some index i such that:
#         arr[0] < arr[1] < ... < arr[i]
#         arr[i] > arr[i+1] > ... > arr[n-1]
#   Return the index of the peak element.
#
# Approach:
#   Use binary search:
#     - Compare arr[mid] with arr[mid + 1].
#     - If arr[mid] < arr[mid + 1],
#         we are on the increasing slope → move right.
#     - Otherwise,
#         we are on the decreasing slope → move left (including mid).
#   Continue until low == high.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low