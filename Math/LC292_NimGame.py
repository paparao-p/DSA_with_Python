"""
Problem: 292. Nim Game
Difficulty: Easy
Pattern: Math / Game Theory

Description
You are playing the Nim Game with n stones.

On each turn, you can remove 1 to 3 stones.
The player who removes the last stone wins.

Return True if you can win the game assuming both players play optimally.

Example:
Input:  n = 4
Output: False

Input:  n = 1
Output: True

Approach
Key observation:
- If n % 4 == 0 → losing position
- Otherwise → winning position

Reason:
You can always force the opponent into multiples of 4.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def canWinNim(self, n: int) -> bool:

        return n % 4 != 0