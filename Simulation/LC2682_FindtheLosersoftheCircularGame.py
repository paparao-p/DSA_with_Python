"""
Problem: 2682. Find the Losers of the Circular Game
Difficulty: Easy
Pattern: Simulation / Hashing

Description
There are n friends sitting in a circle numbered from 1 to n.

Starting from friend 1, the ball is passed in steps:
k, 2k, 3k, ...

Each time, the ball is passed to a new friend in the circle.

The game stops when a friend receives the ball for the second time.

Return a list of all friends who never received the ball.

Example:
Input:  n = 5, k = 2
Output: [4,5]

Explanation:
Visited friends → [1 → 3 → 2 → 4 → 1]
So 4 and 5 never received the ball.
"""


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        visited = [False] * n

        current = 0   # start from index 0 (friend 1)
        step = 1

        while not visited[current]:
            visited[current] = True
            current = (current + step * k) % n
            step += 1

        result = []

        for i in range(n):
            if not visited[i]:
                result.append(i + 1)

        return result