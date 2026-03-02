# LC525 - Contiguous Array
# LeetCode 525 | Medium
# Pattern: Prefix Sum + HashMap


"""
Contiguous Array

Given a binary array nums, return the maximum length of a contiguous
subarray with an equal number of 0 and 1.

Approach:
- Treat 0 as -1 and 1 as +1.
- Maintain a running prefix sum.
- If the same prefix sum appears again,
  the subarray between those indices has equal 0s and 1s.
- Store the first occurrence of each prefix in a hashmap.

Time Complexity: O(n)
Space Complexity: O(n)
"""



class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
         
        prefix = 0
        freq = {0: -1}
        max_sub = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in freq:
                max_sub = max(max_sub, i - freq[prefix])
            else:
                freq[prefix] = i

        return max_sub