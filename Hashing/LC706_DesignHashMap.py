"""
Problem: 706. Design HashMap
Difficulty: Easy
Pattern: Design / Hashing

Description
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
- put(key, value): Insert a (key, value) pair into the HashMap.
                   If the key already exists, update the value.
- get(key): Returns the value to which the specified key is mapped,
            or -1 if this map contains no mapping for the key.
- remove(key): Remove the mapping for the key if it exists.

Constraints:
- 0 <= key, value <= 10^6
- At most 10^4 calls will be made to put, get, and remove.

Approach (Direct Addressing)
1. Use an array of size 10^6 + 1.
2. Use the key directly as the index.
3. Store value at index = key.
4. Use -1 to represent empty/no value.

Time Complexity:
- put   → O(1)
- get   → O(1)
- remove→ O(1)

Space Complexity: O(10^6)
"""


class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)