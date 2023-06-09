class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.snap_id = -1
        self.temp = [0] * length
        self.store = [[0] for _ in range(length)]
        self.snap_store = [[-1] for _ in range(length)]
        self.modify = set()

    def set(self, index: int, val: int) -> None:
        self.temp[index] = val
        self.modify.add(index)

    def snap(self) -> int:
        self.snap_id += 1
        for i in self.modify:
            if self.temp[i] != self.store[i][-1]:
                self.store[i].append(self.temp[i])
                self.snap_store[i].append(self.snap_id)
        self.modify = set()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        l = len(self.snap_store[index])
        low = 0
        high = l - 1
        while low <= high:
            mid = (low + high) // 2
            if self.snap_store[index][mid] == snap_id: 
                return self.store[index][mid]
            elif self.snap_store[index][mid] > snap_id:
                high = mid - 1
            else:
                low = mid + 1
        return self.store[index][low - 1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)