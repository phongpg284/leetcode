class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        res = []
        primes = self.sieve(n)
        for i in range(1, n //2 + 1):
            if primes[i] and primes[n-i]:
                res.append([i, n - i])
        return res
        
    def sieve(self, n):
        primes = [True] * (n + 1)
        primes[0] = False
        primes[1] = False
        p = 2
        while (p * p < n):
            if primes[p]: 
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes 