class RandomizedCollection:
    def __init__(self):
        self.store = []
        self.index_map = defaultdict(list)

    def insert(self, val: int) -> bool:
        self.store.append(val)
        self.index_map[val].append(len(self.store) - 1)
        return len(self.index_map[val]) == 1

    def remove(self, val: int) -> bool:
        if len(self.index_map[val]) == 0:
            return False
        i = self.index_map[val][-1]
        last_item = self.store[-1]
        self.index_map[last_item][-1] = i
        self.index_map[last_item].sort()
        self.store[i] = last_item

        self.store.pop()
        self.index_map[val].pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.store) if len(self.store) > 0 else 0


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
