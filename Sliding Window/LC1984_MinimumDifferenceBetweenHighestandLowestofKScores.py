"""
Problem: 1984. Minimum Difference Between Highest and Lowest of K Scores
Difficulty: Easy
Pattern: Sorting + Sliding Window

Description
You are given an integer array nums, where nums[i] represents the score
of the ith student, and an integer k.

Pick k scores such that the difference between the highest and lowest
of the k scores is minimized.

Return the minimum possible difference.

Example:
Input:  nums = [9,4,1,7], k = 2
Output: 2

Explanation:
Possible pairs:
[1,4] → diff = 3
[4,7] → diff = 3
[7,9] → diff = 2  ✔ (minimum)

Approach
1. Sort the array.
2. Use a sliding window of size k.
3. For each window:
   - Compute difference = nums[i + k - 1] - nums[i]
4. Track the minimum difference.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        # Edge case: only one element selected
        if k == 1:
            return 0

        nums.sort()
        result = float('inf')

        # Sliding window of size k
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            result = min(result, diff)

        return result