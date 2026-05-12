

class ListNode:
    def __init__(self, key, val, nxt = None, prev = None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity

        self.first = None
        self.last = None

        self.key_to_node = {}

    def remove_node(self, node: ListNode):
        key = node.key
        del self.key_to_node[key]

        if node is self.first and node is self.last:
            self.first, self.last = None, None
            return

        if node is self.first:
            node.nxt.prev = None
            self.first = node.nxt
            return

        if node is self.last:
            node.prev.nxt = None
            self.last = node.prev
            return

        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def get(self, key):
        if key in self.key_to_node:
            val = self.key_to_node[key].val

            self.remove_node(self.key_to_node[key])
            self.put(key, val)

            return self.key_to_node[key].val
        else:
             return -1

    def put(self, key, value):
        if key in self.key_to_node:
            self.remove_node(self.key_to_node[key])
            self.put(key, value)
        else:
            if len(self.key_to_node ) == self.capacity:
                self.remove_node(self.first)

            new_node = ListNode(key, value)
            self.key_to_node[key] = new_node

            if not self.first and not self.last:
                self.first, self.last = new_node, new_node
            else:
                new_node.prev = self.last
                self.last.nxt = new_node
                self.last = new_node




# lru = LRUCache(2)
# lru.put(1, 10);  # cache: {1=10}
# print(lru.get(1))     # return 10
# lru.put(2, 20)  # cache: {1=10, 2=20}
# lru.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
# print(lru.get(2))       # returns 20
# print(lru.get(1))      # return -1 (not found)

# lru = LRUCache(3)
# lru.put(1, 1)
# lru.put(2, 2)
# lru.put(3, 3)
# print(lru.get(1))
# print(lru.get(2))
# print(lru.get(3))
# print(lru.get(4))
# lru.put(4, 4)
# print(lru.get(1))
# print(lru.get(2))
# print(lru.get(3))
# print(lru.get(4))

# lru = LRUCache(1)
# lru.put(2, 1)
# print(lru.get(2))
# lru.put(3, 2)
# print(lru.get(2))
# print(lru.get(3))