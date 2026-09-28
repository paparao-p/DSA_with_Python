"""
Problem: 1160. Find Words That Can Be Formed by Characters
Difficulty: Easy
Pattern: Hash Map / Frequency Counting

Description
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars.
Each character in chars can only be used once.

Return the sum of lengths of all good strings in words.

Example:
Input:  words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6

Explanation:
"cat" → valid (uses 'c','a','t')
"hat" → valid (uses 'h','a','t')
"bt" → invalid
"tree" → invalid
Total length = 3 + 3 = 6

Approach
1. Count frequency of characters in chars.
2. For each word:
   - Make a copy of the frequency map.
   - Check if all characters in the word can be formed.
   - If valid → add its length to result.
3. Return total length.

Time Complexity: O(n * k)
    n = number of words
    k = average word length

Space Complexity: O(1)
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        # Frequency map for chars
        mapping = {}
        for char in chars:
            mapping[char] = mapping.get(char, 0) + 1

        count = 0

        for word in words:

            temp = mapping.copy()

            for char in word:
                if char not in temp or temp[char] == 0:
                    break
                temp[char] -= 1
            else:
                count += len(word)

        return count
