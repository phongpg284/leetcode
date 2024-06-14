class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = encoding
        self.encode_index = -1
        self.max_index = -1
        self.cur_index = -1

    def next(self, n: int) -> int:
        self.cur_index += n
        while self.max_index < self.cur_index:
            self.encode_index += 2
            if self.encode_index >= len(self.arr):
                return -1
            self.max_index += self.arr[self.encode_index - 1]
        return self.arr[self.encode_index]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
