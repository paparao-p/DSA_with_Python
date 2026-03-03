# LC930 - Binary Subarrays With Sum
# LeetCode 930 | Medium
# Pattern: Prefix Sum + HashMap


"""
Binary Subarrays With Sum

Given a binary array nums and an integer goal,
return the number of non-empty subarrays with sum equal to goal.

Approach:
- Maintain running prefix sum.
- Use a hashmap to store frequency of prefix sums.
- If (current_prefix - goal) exists in hashmap,
  then there exists a subarray ending at current index
  whose sum equals goal.
- Add its frequency to the result.

Time Complexity: O(n)
Space Complexity: O(n)
"""



class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefix = 0
        freq = {0: 1}
        count = 0

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix - goal in freq:
                count += freq[prefix - goal]

            if prefix not in freq:
                freq[prefix] = 1
            else:
                freq[prefix] += 1
          
        return count