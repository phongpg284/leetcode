import math
class Solution:
    def numSquares(self, n: int) -> int:
        map = dict()
        return self.find_squares(n, map)

    def find_squares(self, n, map):
        if n <= 1:
            return n
        result = float('inf')
        f = math.floor(math.sqrt(n))
        for i in range(f, f//2, -1):
            left = n - i * i
            if left in map:
                result = min(result, map[left] + 1)
            else:
                temp = self.find_squares(left, map)
                map[left] = temp
                result = min(result, temp + 1)
        return result