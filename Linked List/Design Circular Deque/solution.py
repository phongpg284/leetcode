class MyCircularDeque:
    def __init__(self, k: int):
        self.q = [-1] * (k + 1)
        self.front = 0
        self.last = 1
        self.size = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False

        self.q[self.front] = value
        self.front = (self.front + self.k - 1) % self.k
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False

        self.q[self.last] = value
        self.last = (self.last + self.k + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        self.front = (self.front + self.k + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False

        self.last = (self.last + self.k - 1) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.q[(self.front + self.k + 1) % self.k] if self.size > 0 else -1

    def getRear(self) -> int:
        return self.q[(self.last + self.k - 1) % self.k] if self.size > 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
