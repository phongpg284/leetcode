mod = 10 ** 9 + 7
class Solution:
    def countOrders(self, n: int) -> int:
        '''
            For every new pair (Pn , Dn), we have (2i + 1) place to place Pn between (Pi, Di) with i from 1 to n-1
            With each place of Dn, we can place Dn in 1, 2, ....., 2i + 1 place after Pn
            Therefore, we have 1 + 2 + ... + (2i + 1) = (2i + 1)(i + 1) way to place new (Pn, Dn) pair
            So, dp[i + 1] = dp[i] * (2i + 1) * (i + 1)
        '''

        res = 1                                             
        for i in range (n):
            res = res * (2* i + 1) * (i + 1) % mod
        return res