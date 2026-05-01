"""
Problem: 1207. Unique Number of Occurrences
Difficulty: Easy
Pattern: Hash Map + Set

Description
Given an array of integers arr, return True if the number of occurrences
of each value in the array is unique, otherwise return False.

Example:
Input:  arr = [1,2,2,1,1,3]
Output: True

Explanation:
Occurrences:
1 → 3 times
2 → 2 times
3 → 1 time
All frequencies are unique.

Input:  arr = [1,2]
Output: False

Approach
1. Count frequency of each number using a hashmap.
2. Extract all frequency values.
3. Convert them into a set.
4. If set size == number of values → all frequencies are unique.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        mapping = {}

        # Count frequency of elements
        for num in arr:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        # Check uniqueness of frequencies
        return len(set(mapping.values())) == len(mapping.values())
