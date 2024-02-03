class MyQueue:

    def __init__(self):
        self.q = list()
        self.n = 0
        self.i = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.n += 1

    def pop(self) -> int:
        self.i += 1
        return self.q[self.i - 1]

    def peek(self) -> int:
        return self.q[self.i]

    def empty(self) -> bool:
        return self.i == self.n


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
