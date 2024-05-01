class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        store = defaultdict(list)
        m, n = len(key), len(ring)
        dp = [[-1] * n for _ in range(m)]

        for i, c in enumerate(ring):
            store[c].append(i)
        return self.helper(0, 0, store, key, ring, n, dp)

    def helper(self, i, pos, store, key, ring, n, dp):
        if i == len(key):
            return 0

        if dp[i][pos] > -1:
            return dp[i][pos]

        res = float('inf')

        for j in store[key[i]]:
            if j >= pos:
                steps = min(j - pos, pos + n - j)
            else:
                steps = min(pos - j, j + n - pos)

            res = min(res, steps + self.helper(i +
                      1, j, store, key, ring, n, dp))

        dp[i][pos] = res + 1
        return res + 1
