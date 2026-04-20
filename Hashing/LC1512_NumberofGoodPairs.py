"""
Problem: 1512. Number of Good Pairs
Difficulty: Easy
Pattern: Hash Map / Frequency Counting

Description
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if:
- nums[i] == nums[j]
- i < j

Example:
Input:  nums = [1,2,3,1,1,3]
Output: 4

Explanation:
Good pairs are:
(0,3), (0,4), (3,4), (2,5)

Approach
1. Use a hashmap to store frequency of elements.
2. For each number:
   - If already seen → add its frequency to count
   - Then increase its frequency
3. This counts all valid (i < j) pairs efficiently.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        freq = {}
        count = 0

        for num in nums:

            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1

        return count