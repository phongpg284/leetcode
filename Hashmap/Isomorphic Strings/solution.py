class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        store = {}
        reverse_store = {}

        for i in range(n):
            if s[i] in store and t[i] != store[s[i]]:
                return False
            if t[i] in reverse_store and reverse_store[t[i]] != s[i]:
                return False

            store[s[i]] = t[i]
            reverse_store[t[i]] = s[i]
        return True
