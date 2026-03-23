"""
Problem: 862. Shortest Subarray with Sum at Least K
Difficulty: Hard
Pattern: Prefix Sum + Monotonic Deque

Description
Given an integer array nums and an integer k, return the length of the
shortest non-empty subarray of nums with a sum of at least k.

If there is no such subarray, return -1.

Example:
Input:  nums = [2,-1,2], k = 3
Output: 3

Input:  nums = [1,2], k = 4
Output: -1

Approach
1. Compute prefix sum array.
   prefix[i] = sum of nums[0..i-1]

2. Use a deque to maintain indices of prefix sums in increasing order.

3. For each index j:
   - Check if current prefix minus smallest prefix ≥ k.
     → Update result and pop from front.
   - Maintain monotonic increasing order:
     → Remove larger prefix sums from back.
   - Add current index to deque.

Why it works:
- We want the smallest subarray → smallest length → earliest valid prefix
- Monotonic deque helps efficiently maintain useful candidates

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # Step 1: Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()  # stores indices of prefix
        result = n + 1

        # Step 2: Process prefix array
        for j in range(n + 1):

            # Check if valid subarray found
            while dq and prefix[j] - prefix[dq[0]] >= k:
                result = min(result, j - dq.popleft())

            # Maintain increasing prefix values
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(j)

        return result if result != n + 1 else -1