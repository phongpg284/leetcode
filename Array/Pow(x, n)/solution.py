class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        is_negative = False
        if n < 0:
            is_negative = True
            n = -n
        
        res = 1
        
        while n > 0:
            cur = x
            count = 1

            while count * 2 <= n:
                count *= 2
                cur = cur * cur
            n-= count
            res *= cur

        if is_negative:
            return 1/res
        return res        
