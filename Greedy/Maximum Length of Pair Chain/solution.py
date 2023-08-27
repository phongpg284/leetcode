# Greedy solution
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, ans = float('-inf'), 0
        
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                ans += 1
                
        return ans
    


# DP solution
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1] * n
        
        for i in range(1, n):
            dp[i] = max(dp[i], max(dp[j] + 1 if pairs[i][0] > pairs[j][1] else 1 for j in range(i)))
        
        return max(dp)