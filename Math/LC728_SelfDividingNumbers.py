"""
Problem: 728. Self Dividing Numbers
Difficulty: Easy
Pattern: Math / Digit Processing

Description
A self-dividing number is a number that is divisible by every digit it contains.

Conditions:
- The number should not contain the digit 0.
- Each digit must divide the number evenly.

Return a list of all self-dividing numbers in the range [left, right].

Example:
Input:  left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Explanation:
- 12 → digits 1 and 2 → divisible by both ✔
- 15 → digits 1 and 5 → divisible by both ✔
- 10 → contains 0 ❌
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def is_self_dividing(num: int) -> bool:
            temp = num

            while temp > 0:
                digit = temp % 10

                # digit should not be 0 and must divide num
                if digit == 0 or num % digit != 0:
                    return False

                temp //= 10

            return True

        result = []

        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)

        return result