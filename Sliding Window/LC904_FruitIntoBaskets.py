# LeetCode 904 - Fruit Into Baskets
# Pattern: Sliding Window + Hash Map
#
# Problem:
#   You are given an array fruits where fruits[i] is the type of fruit
#   the i-th tree produces.
#   You can collect fruits from a contiguous subarray, but you can only
#   carry two types of fruits in your baskets.
#   Return the maximum number of fruits you can pick.
#
# Approach:
#   Use a sliding window with two pointers:
#     - Expand the right pointer and add fruits[right] to a hashmap.
#     - The hashmap keeps counts of fruit types inside the window.
#     - If the number of distinct fruit types exceeds 2,
#       shrink the window from the left until it becomes valid again.
#     - Track the maximum window length during the process.
#
# Time Complexity: O(n)
# Space Complexity: O(1)   # at most 2 keys in the hashmap


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        freq = {}
        left = 0
        max_len = 0
        distinct = 0

        for right in range(len(fruits)):

            if fruits[right] not in freq:
                freq[fruits[right]] = 1
                distinct += 1
            else:
                freq[fruits[right]] += 1

            while distinct > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                    distinct -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
