"""
Problem: 506. Relative Ranks
Difficulty: Easy
Pattern: Sorting + Hash Map

Description
You are given an integer array score where score[i] is the score of the ith athlete.

Return an array answer such that:
- The highest score gets "Gold Medal"
- The second highest gets "Silver Medal"
- The third highest gets "Bronze Medal"
- The rest get their rank number (as a string)

Example:
Input:  score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Approach
1. Sort the scores in descending order.
2. Assign ranks:
   - Top 3 → medals
   - Others → rank number as string
3. Store mapping of score → rank.
4. Build result using original order.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        # Sort scores in descending order
        sorted_scores = sorted(score, reverse=True)

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_map = {}

        # Assign ranks
        for i, val in enumerate(sorted_scores):
            if i < 3:
                rank_map[val] = medals[i]
            else:
                rank_map[val] = str(i + 1)

        # Build result in original order
        return [rank_map[num] for num in score]