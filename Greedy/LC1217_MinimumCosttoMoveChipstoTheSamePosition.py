"""
Problem: 1217. Minimum Cost to Move Chips to The Same Position
Difficulty: Easy
Pattern: Greedy / Counting

Description
We have n chips, where the position of the ith chip is position[i].

We can move a chip:
- By 2 positions → cost = 0
- By 1 position → cost = 1

Return the minimum cost needed to move all chips to the same position.

Example:
Input:  position = [1,2,3]
Output: 1

Input:  position = [2,2,2,3,3]
Output: 2

Approach
Key observation:
- Moving chips between positions of the same parity (even ↔ even or odd ↔ odd) costs 0.
- Moving between different parity (even ↔ odd) costs 1.

So:
1. Count how many chips are at even positions.
2. Count how many chips are at odd positions.
3. Move the smaller group to the larger group.

Result = min(even_count, odd_count)

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        even = 0
        odd = 0

        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)