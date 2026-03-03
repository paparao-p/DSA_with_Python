# LC523 - Continuous Subarray Sum
# LeetCode 523 | Medium
# Pattern: Prefix Sum + HashMap (Remainder Technique)


"""
Continuous Subarray Sum

Given an integer array nums and an integer k,
return True if nums has a continuous subarray of size
at least 2 whose elements sum up to a multiple of k.

Approach:
- Maintain running prefix sum.
- Compute remainder = prefix % k.
- If the same remainder appears again,
  then the subarray between those indices
  is divisible by k.
- Ensure subarray length >= 2.
- Store only the first occurrence of each remainder.

Time Complexity: O(n)
Space Complexity: O(min(n, k))
"""



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = 0
        freq = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k

            if rem in freq:
                if i - freq[rem] >= 2:
                    return True
            else:
                freq[rem] = i

        return False