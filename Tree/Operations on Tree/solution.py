class LockingTree:

    def __init__(self, parent: List[int]):
        self.lock_store = [False] * len(parent)
        self.tree = defaultdict(list)
        self.parent = parent
        for i in range(len(parent)):
            self.tree[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.lock_store[num]:
            return False
        self.lock_store[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.lock_store[num] != user:
            return False
        self.lock_store[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        temp = num
        while temp != -1:
            if self.lock_store[temp]:
                return False
            temp = self.parent[temp]

        q = deque([num])
        has_child_lock = False
        while q:
            node = q.popleft()
            for child in self.tree[node]:
                if self.lock_store[child]:
                    self.lock_store[child] = None
                    has_child_lock = True
                q.append(child)

        if has_child_lock:
            self.lock(num, user)
            return True
        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
