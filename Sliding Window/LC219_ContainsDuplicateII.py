# LeetCode 219 - Contains Duplicate II
# Pattern: Sliding Window + Hash Set
#
# Problem:
#   Given an integer array nums and an integer k,
#   return true if there are two distinct indices i and j
#   such that:
#     - nums[i] == nums[j]
#     - abs(i - j) <= k
#
# Approach:
#   Use a sliding window of size at most k:
#     - Traverse the array with index `right`.
#     - Maintain a set containing elements in the current window.
#     - If nums[right] already exists in the set, a duplicate
#       within distance k is found.
#     - Add nums[right] to the set.
#     - If window size exceeds k, remove nums[left] and
#       increment left pointer.
#
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        left = 0

        for right in range(len(nums)):

            if nums[right] in window:
                return True

            window.add(nums[right])

            # Keep window size <= k
            if right - left >= k:
                window.remove(nums[left])
                left += 1

        return False
