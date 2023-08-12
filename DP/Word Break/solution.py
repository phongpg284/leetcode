class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        wordDict = set(wordDict)
        return self.dfs(s, wordDict, dp)
    
    def dfs(self, s, wordDict, dp):
        if s in dp:
            return dp[s] 
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in wordDict and self.dfs(s[i:], wordDict, dp):
                dp[s] = True
                return True
        dp[s] = False
        return False