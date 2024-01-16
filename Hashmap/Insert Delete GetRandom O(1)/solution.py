class RandomizedSet:

    def __init__(self):
        self.store = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.store.append(val)
        self.index_map[val] = len(self.store) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        i = self.index_map[val]
        last_item = self.store[-1]
        self.store[i] = last_item
        self.index_map[last_item] = i

        self.store.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.store)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
