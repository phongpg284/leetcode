class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        temp = n - 1
        pos = 1

        while temp:
            if not (x & pos):
                res |= (temp & 1) * pos
                temp >>= 1
            pos <<= 1

        return res
