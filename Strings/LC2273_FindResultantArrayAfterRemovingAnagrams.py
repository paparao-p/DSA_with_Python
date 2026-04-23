"""
Problem: 2273. Find Resultant Array After Removing Anagrams
Difficulty: Easy
Pattern: String + Sorting / Hashing

Description
You are given a 0-indexed string array words.

In one operation, you can remove words[i] if it is an anagram of
words[i - 1].

Return the array after performing all possible removals.

Example:
Input:  words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]

Explanation:
- "baba" is an anagram of "abba" → remove
- "bbaa" is an anagram of "abba" → remove
- "cd" stays
- Next "cd" is an anagram of previous "cd" → remove

Approach
1. Keep track of previous word’s sorted form.
2. For each word:
   - Sort characters → get canonical form
   - If different from previous → keep it
3. Update previous sorted word.

Time Complexity: O(n * k log k)
    n = number of words
    k = length of each word

Space Complexity: O(n)
"""


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        result = []
        prev = ""

        for word in words:

            # Get sorted representation
            curr_sorted = ''.join(sorted(word))

            # Compare with previous
            if curr_sorted != prev:
                result.append(word)
                prev = curr_sorted

        return result