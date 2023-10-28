class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            next_a = (e + i + u) % mod
            next_e = (a + i) % mod
            next_i = (e + o) % mod
            next_o = i % mod
            next_u = (i + o) % mod
            a, e, i, o, u = next_a, next_e, next_i, next_o, next_u
        return (a + e + i + o + u) % mod