# LC560 - Subarray Sum Equals K
# LeetCode 560 | Medium
# Pattern: Prefix Sum + HashMap


"""
Subarray Sum Equals K

Given an integer array nums and an integer k,
return the total number of subarrays whose sum equals to k.

Approach:
- Build prefix sum while iterating.
- Use a frequency hashmap to store how many times
  a prefix sum has appeared.
- If (current_prefix - k) exists in hashmap,
  add its frequency to count.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # prefix = [0] * (len(nums) + 1)
        # freq = {0: 1}
        # count = 0

        # for i in range(len(nums)):
        #     prefix[i + 1] = prefix[i] + nums[i]
        
        #     a = prefix[i + 1] - k
        #     if a in freq:
        #         count += freq[a]

        #     if prefix[i + 1] not in freq:
        #         freq[prefix[i + 1]] = 1
        #     else:
        #         freq[prefix[i + 1]] += 1

        # return count

        prefix = 0
        freq = {0:1}
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix-k in freq:
                count += freq[prefix-k]
   
            if prefix not in freq:
                freq[prefix] = 1
            else:
                freq[prefix] += 1
          
        return count