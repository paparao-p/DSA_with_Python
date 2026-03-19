"""
Problem: 49. Group Anagrams
Difficulty: Medium
Pattern: Hash Map / Frequency Signature

Description
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An anagram is a word formed by rearranging the letters of another word,
using all the original letters exactly once.

Example:
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Approach (Sorting Key)
1. For each word, sort its characters.
2. Use the sorted string as a key in a hashmap.
3. Append the original word to the corresponding group.

Words that are anagrams will have the same sorted key.

Time Complexity: O(n * k log k)
    n = number of words
    k = average length of each word

Space Complexity: O(n * k)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            mapping[key].append(word)

        return list(mapping.values())