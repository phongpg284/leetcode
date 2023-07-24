class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        # mark if n is negative
        is_negative = False
        if n < 0:
            is_negative = True
            n = -n
        
        res = 1
        
        while n > 0:
            cur = x
            count = 1
            # multiple until meet x^n using cur ** 2 to reduce time complecity to log n)            
            while count * 2 <= n:
                count *= 2
                cur = cur * cur
            n-= count
            res *= cur

        # if n is negative return 1/res
        if is_negative:
            return 1/res
        return res        
