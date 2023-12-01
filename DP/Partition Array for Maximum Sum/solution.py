class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * (n + 1)
        return self.helper(arr, k, 0, n, dp)

    def helper(self, arr, k, start, n, dp):
        if dp[start] > -1:
            return dp[start]

        res = 0
        val = 0
        for i in range(min(k, n - start)):
            val = arr[start + i] if arr[start + i] > val else val
            temp = self.helper(arr, k, start + i + 1, n, dp) + val * (i + 1)
            res = temp if temp > res else res
        
        dp[start] = res
        return res