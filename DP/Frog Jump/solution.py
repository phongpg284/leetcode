class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        store = {stones[i]: i for i in range(n)}
        dp = [[-1] * n for _ in range(n)]

        if stones[1] - stones[0] != 1:
            return False
        return self.helper(store, dp, stones, 1, 1)

    def helper(self, store, dp, stones, i, k):
        if i == len(stones) - 1:
            return True

        if dp[i][k] != -1:
            return dp[i][k] == 1

        k_cur, k_prev, k_next = False, False, False

        if stones[i] + k in store:
            k_cur = self.helper(store, dp, stones, store[stones[i] + k], k)

        if k > 1 and stones[i] + k - 1 in store:
            k_prev = self.helper(
                store, dp, stones, store[stones[i] + k - 1], k - 1)

        if stones[i] + k + 1 in store:
            k_next = self.helper(
                store, dp, stones, store[stones[i] + k + 1], k + 1)

        dp[i][k] = 1 if k_cur or k_prev or k_next else 0
        return dp[i][k] == 1
