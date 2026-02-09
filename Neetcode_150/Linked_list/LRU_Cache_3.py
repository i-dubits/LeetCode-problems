class ListNode:
    def __init__(self, key, val, nxt = None, prev = None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}

        # fictitious first node
        self.first = ListNode(-1, -1)
        # fictitious last node
        self.last = ListNode(-1, -1)

        self.first.nxt = self.last
        self.last.prev = self.first

    def insert_node(self, node:ListNode):

        node.prev = self.last.prev
        self.last.prev.nxt = node
        node.nxt = self.last

        self.last.prev = node

    def remove_node_from_list(self, node:ListNode):
        """Deattach node from the double linked list.
        This method does not remove it from self.key_to_node dictionary!"""
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def get(self, key):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            val = node.val
            self.remove_node_from_list(node)
            self.insert_node(node)

            return val
        else:
            return -1


    def put(self, key, value):

        if self.capacity == 0:
            return

        if key in self.key_to_node:
            self.remove_node_from_list(self.key_to_node[key])

            new_node = self.key_to_node[key]
            new_node.val = value
            self.insert_node(new_node)

        else:
            if self.capacity == len(self.key_to_node):
                node_to_remove = self.first.nxt
                self.remove_node_from_list(node_to_remove)

                # The complete node removal happens only here
                del self.key_to_node[node_to_remove.key]

                new_node = ListNode(key, value)
                self.insert_node(new_node)
                self.key_to_node[key] = new_node

            else:
                new_node = ListNode(key, value)
                self.insert_node(new_node)
                self.key_to_node[key] = new_node



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

# lru = LRUCache(2)
# lru.put(1, 1)
# lru.put(2, 2)
# print(lru.get(1))
# lru.put(3, 3)
# print(lru.get(1))
# print(lru.get(2))
# print(lru.get(3))
# print(lru.get(1))
# lru.put(4, 4)
# print(lru.get(1))
# print(lru.get(3))
# print(lru.get(4))
