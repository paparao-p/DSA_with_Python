# LC974 - Subarray Sums Divisible by K
# LeetCode 974 | Medium
# Pattern: Prefix Sum + HashMap (Remainder Technique)


"""
Subarray Sums Divisible by K

Given an integer array nums and an integer k,
return the number of non-empty subarrays whose sum is divisible by k.

Approach:
- Maintain running prefix sum.
- Compute remainder = prefix % k.
- If the same remainder has appeared before,
  then the subarray between those indices is divisible by k.
- Use a hashmap to store frequency of remainders.

Time Complexity: O(n)
Space Complexity: O(k)
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        freq = {0: 1}
        count = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]

            # (curr_sum - prev_sum) % k == 0
            reminder = prefix % k

            if reminder in freq:
                count += freq[reminder]
                freq[reminder] += 1
            else:
                freq[reminder] = 1

        return count