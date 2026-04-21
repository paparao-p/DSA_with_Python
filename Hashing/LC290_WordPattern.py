"""
Problem: 290. Word Pattern
Difficulty: Easy
Pattern: Hash Map / Bi-directional Mapping

Description
Given a pattern and a string s, determine if s follows the same pattern.

Here, "follow" means a full match, such that:
- There is a bijection between a letter in pattern and a word in s.

Example:
Input:  pattern = "abba", s = "dog cat cat dog"
Output: True

Input:  pattern = "abba", s = "dog cat cat fish"
Output: False

Input:  pattern = "aaaa", s = "dog cat cat dog"
Output: False

Approach
1. Split the string s into words.
2. If lengths mismatch → return False.
3. Use two hash maps:
   - pattern → word
   - word → pattern
4. Check consistency in both directions.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        
        # length mismatch
        if len(pattern) != len(words):
            return False
        
        p_to_w = {}
        w_to_p = {}
        
        for p, w in zip(pattern, words):
            
            # check pattern → word
            if p in p_to_w:
                if p_to_w[p] != w:
                    return False
            else:
                p_to_w[p] = w
            
            # check word → pattern
            if w in w_to_p:
                if w_to_p[w] != p:
                    return False
            else:
                w_to_p[w] = p
        
        return True