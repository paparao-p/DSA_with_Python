"""
Problem: 2379. Minimum Recolors to Get K Consecutive Black Blocks
Difficulty: Easy
Pattern: Sliding Window (Fixed Size)

Description
You are given a string blocks where:
- 'B' represents a black block
- 'W' represents a white block

You are also given an integer k.

In one operation, you can change a white block to a black block.

Return the minimum number of operations needed to get at least
one substring of k consecutive black blocks.

Example:
Input:  blocks = "WBBWWBBWBW", k = 7
Output: 3

Explanation:
We need at least 7 consecutive 'B's.
Minimum whites in any window of size 7 → 3 → recolor those.

Approach
1. Use a sliding window of size k.
2. Count number of 'W' (white blocks) in the current window.
3. Minimum whites in any window = minimum operations needed.
4. Slide the window across the string.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        left = 0
        white = 0
        result = float("inf")

        for right in range(len(blocks)):

            # Count white blocks in window
            if blocks[right] == "W":
                white += 1

            # Maintain window size = k
            if right - left + 1 == k:

                # Update result
                result = min(result, white)

                # Remove left element
                if blocks[left] == "W":
                    white -= 1

                left += 1

        return result