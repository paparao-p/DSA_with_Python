"""
Problem: 682. Baseball Game
Difficulty: Easy
Pattern: Stack Simulation

Description
You are keeping track of a baseball game's score with unusual rules.

Given a list of strings `operations`, where each operation is one of the following:

Integer x  -> Record a new score of x
"+"        -> Record a new score that is the sum of the previous two scores
"D"        -> Record a new score that is double the previous score
"C"        -> Invalidate the previous score and remove it

Return the total score after all operations.

Approach
Use a stack to store valid scores.

Rules:
1. If operation is an integer → push it to stack.
2. "C" → remove the last score.
3. "D" → push double of the last score.
4. "+" → push sum of last two scores.

Maintain a running `total` so we don't need to sum the stack at the end.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        total = 0

        for op in operations:

            if op == "C":
                removed = stack.pop()
                total -= removed

            elif op == "D":
                stack.append(stack[-1] * 2)
                total += stack[-1]

            elif op == "+":
                stack.append(stack[-1] + stack[-2])
                total += stack[-1]

            else:
                stack.append(int(op))
                total += stack[-1]

        return total