mod = 10 ** 9 + 7
class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range (n):
            res = res * (2* i + 1) * (i + 1) % mod
        return res