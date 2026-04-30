"""
Problem: 1248. Count Number of Nice Subarrays
Difficulty: Medium
Pattern: Prefix Sum + Hash Map

Description
Given an array of integers nums and an integer k, return the number of
"nice" subarrays.

A subarray is called nice if it contains exactly k odd numbers.

Example:
Input:  nums = [1,1,2,1,1], k = 3
Output: 2

Explanation:
Nice subarrays are:
[1,1,2,1]
[1,2,1,1]

Approach
1. Convert the problem:
   - Treat odd numbers as 1
   - Treat even numbers as 0
2. Now the problem becomes:
   → Count subarrays with sum = k
3. Use prefix sum + hashmap:
   - prefix_sum tracks number of odd numbers so far
   - freq stores counts of prefix sums
4. For each prefix_sum:
   - If (prefix_sum - k) exists → add its frequency

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0

        # prefix_sum frequency map
        freq = {0: 1}

        for num in nums:

            # Convert odd/even → 1/0
            prefix_sum += num % 2

            # Check if there exists a subarray with k odds
            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            # Update frequency map
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count