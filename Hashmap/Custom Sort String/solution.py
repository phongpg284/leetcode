class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        store = {}

        for c in s:
            store[c] = store.get(c, 0) + 1

        for c in order:
            if c in store:
                res += c * store[c]
                del store[c]

        for c, count in store.items():
            res += c * count

        return res
