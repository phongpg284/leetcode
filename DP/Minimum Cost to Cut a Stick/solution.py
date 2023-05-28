class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[0] * (m) for _ in range(m)]
        res = self.helper(0, m - 1, cuts, dp)
        return res

    def helper(self, start, end, cuts, dp):
        if dp[start][end] > 0:
            return dp[start][end]
        result = float(inf)
        for i in range(start + 1, end): 
            left_cut = self.helper(start, i, cuts, dp)
            right_cut = self.helper(i, end, cuts, dp)
            result = min(result, left_cut + right_cut + cuts[end] - cuts[start])
        if result == float(inf):
            return 0
        dp[start][end] = result
        return result