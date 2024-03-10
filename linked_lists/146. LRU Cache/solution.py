from collections import deque

# this is not a good solution because the remove operation is O(n)
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.capacity = capacity
#         self.order = deque()  # orderをdequeに変更

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.order.remove(key)  # dequeでもremove操作は可能
#             self.order.append(key)  # 最も最近使用された要素を末尾に移動
#             return self.cache[key]
#         else: 
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.order.remove(key)  # 既存のキーをorderから削除
#             self.order.append(key)  # 最も最近使用された要素を末尾に追加
#             self.cache[key] = value
#         else:
#             if len(self.cache) >= self.capacity:
#                 oldestKey = self.order.popleft()  # dequeのpopleftを使用して最も古い要素を削除
#                 del self.cache[oldestKey]
#             self.order.append(key)  # 新しいキーを末尾に追加
#             self.cache[key] = value

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
