class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        res = max(abs(fx - sx), abs(fy - sy))
        if res == 0 and t == 1:
            return False
        return res <= t