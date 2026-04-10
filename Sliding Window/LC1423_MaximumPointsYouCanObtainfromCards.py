"""
Problem: 1423. Maximum Points You Can Obtain from Cards
Difficulty: Medium
Pattern: Sliding Window (Complement Window)

Description
There are several cards arranged in a row, and each card has an associated number of points.

Given an integer array cardPoints and an integer k,
you can take exactly k cards from either the beginning or the end of the row.

Return the maximum score you can obtain.

Example:
Input:  cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12

Explanation:
Take last 3 cards → [6,5,1] → sum = 12

Approach
Instead of selecting k cards from ends,
think of removing a subarray of size (n - k) from the middle.

1. Total sum of all cards.
2. Find minimum subarray sum of size (n - k).
3. Result = total_sum - min_subarray_sum

This converts the problem into a sliding window problem.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)

        # If we take all cards
        if k == n:
            return sum(cardPoints)

        total_sum = sum(cardPoints)

        window_size = n - k
        curr_sum = 0

        # First window
        for i in range(window_size):
            curr_sum += cardPoints[i]

        min_sum = curr_sum

        # Slide window
        for i in range(window_size, n):
            curr_sum += cardPoints[i]
            curr_sum -= cardPoints[i - window_size]
            min_sum = min(min_sum, curr_sum)

        return total_sum - min_sum