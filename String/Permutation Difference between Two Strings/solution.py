class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        store = {s[i]: i for i in range(len(s))}
        res = 0
        for i in range(len(t)):
            res += abs(store[t[i]] - i)
        return res
