"""
Problem: 239. Sliding Window Maximum
Difficulty: Hard
Pattern: Monotonic Deque / Sliding Window

Description
Given an array nums and an integer k, return the maximum value
in each sliding window of size k.

Example:
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation:
Window [1,3,-1] → max = 3
Window [3,-1,-3] → max = 3
Window [-1,-3,5] → max = 5
...

Approach (Monotonic Deque)
Use a deque to store indices of elements in decreasing order.

1. Remove indices that are out of the current window.
2. Remove elements smaller than current element (they are useless).
3. Add current index to deque.
4. The front of deque always contains the index of the maximum element.
5. Append it to result when window size is reached.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):

            # Remove elements outside the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Add result once window is valid
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result