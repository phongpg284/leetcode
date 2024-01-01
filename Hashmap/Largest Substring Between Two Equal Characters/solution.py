class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        store = dict()
        start, end = 0, 0
        for i, c in enumerate(s):
            if c not in store:
                store[c] = []
            store[c].append(i)

        for c in store.keys():
            pos = store[c]
            if len(pos) >= 2 and pos[-1] - pos[0] > end - start:
                start = pos[0]
                end = pos[-1]

        return end - start - 1
