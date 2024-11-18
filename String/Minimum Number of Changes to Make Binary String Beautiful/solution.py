class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        res = 0 

        for i in range(0, n, 2):
            res += 1 if s[i] != s[i + 1] else 0
        
        return res
