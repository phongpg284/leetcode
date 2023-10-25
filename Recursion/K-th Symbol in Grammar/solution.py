class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        res = 0
        while n > 1:
            if k % 2 == 0:
                res = 1 - res
            k = (k + 1) // 2
            n -= 1

        return res