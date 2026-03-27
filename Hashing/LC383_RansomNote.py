"""
Problem: 383. Ransom Note
Difficulty: Easy
Pattern: Hash Map / Frequency Counting

Description
Given two strings ransomNote and magazine, return True if ransomNote
can be constructed by using the letters from magazine.

Each letter in magazine can only be used once.

Example:
Input:  ransomNote = "a", magazine = "b"
Output: False

Input:  ransomNote = "aa", magazine = "aab"
Output: True

Approach
1. Count the frequency of characters in ransomNote using a hashmap.
2. Traverse the magazine string:
   - If the character exists in hashmap, decrease its count.
   - Remove it when count becomes zero.
3. If hashmap becomes empty, return True.
4. Otherwise, return False.

Time Complexity: O(n + m)
Space Complexity: O(1) (at most 26 lowercase letters)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mapping = {}

        # Count characters in ransomNote
        for char in ransomNote:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        # Match characters using magazine
        for char in magazine:
            if char in mapping:
                mapping[char] -= 1

                if mapping[char] == 0:
                    mapping.pop(char)

                    # Early exit if all characters matched
                    if not mapping:
                        return True

        return not mapping