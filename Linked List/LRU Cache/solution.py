class CacheItem:
    def __init__(self, val = 0, key = 0, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.last = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        before = node.prev
        after = node.next
        if not before:
            return node.val
        if before:
            if node == self.last:
                self.last = before
            before.next = after
        if after:
            after.prev = before
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.head.prev = None
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            before = node.prev
            after = node.next
            if node == self.head:
                node.val = value
                return
            if before:
                if node == self.last:
                    self.last = before
                before.next = after
            if after:
                after.prev = before
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
            self.head.val = value
        else:
            if self.count < self.capacity:
                self.count += 1
            else:
                if self.last and self.last.key in self.cache:
                    self.cache.pop(self.last.key)
                    self.last = self.last.prev
                    if self.last:
                        self.last.next = None
            new_node = CacheItem(value, key)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            new_node.prev = None
            self.head = new_node
            self.cache[key] = new_node
            if self.count == 1:
                self.last = new_node
                self.last.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)