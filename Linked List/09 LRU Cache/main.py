class Node:
    def __init__(self, key:int, val:int) -> None:
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key to node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node:Node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def remove(self, node:Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def insert(self, node:Node): # insert at right
        prev, nxt = self.right.prev, self.right
        prev.next  = nxt.prev = node
        node.next, node.prev = nxt, prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]




# ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
lru = LRUCache(2)
print(lru.put(1, 1), end=" ")
print(lru.put(2, 2), end=" ")
print(lru.get(1), end=" ")
print(lru.put(3, 3), end=" ")
print(lru.get(2), end=" ")
print(lru.put(4, 4), end=" ")
print(lru.get(1), end=" ")
print(lru.get(3), end=" ")
print(lru.get(4), end=" ")



# LRU Cache
#
# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
#
#     LRUCache(int capacity) Initialize the LRU cache of size capacity.
#     int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
#
# A key is considered used if a get or a put operation is called on it.
#
# Ensure that get and put each run in O(1)O(1) average time complexity.
#
# Example 1:
#
# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
#
# Output:
# [null, null, 10, null, null, 20, -1]
#
# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20
# lRUCache.get(1);      // return -1 (not found)
#
# Constraints:
#
#     1 <= capacity <= 100
#     0 <= key <= 1000
#     0 <= value <= 1000
