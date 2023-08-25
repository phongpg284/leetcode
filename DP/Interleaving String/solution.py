class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        dp = [[0] * (n + 1) for _ in range(m + 1)] 
        def recur(i, j, k):
            if dp[i][j] != 0:
                if dp[i][j] == 1:
                    return True
                else: 
                    return False

            if k == p:
                if i == m and j == n:
                    return True
                else:
                    dp[i][j] = -1
                    return False
            if i < m and s1[i] == s3[k]:
                temp = s1[i]
                i += 1
                k += 1
                if recur(i, j ,k):
                    dp[i][j] = 1
                    return True
                i -= 1
                k -= 1
            
            if j < n and s2[j] == s3[k]:
                temp = s2[j]
                j += 1
                k += 1
                if recur(i, j , k):
                    dp[i][j] = 1
                    return True
                j -= 1
                k -= 1
            dp[i][j] = -1
            return False
        return recur(0, 0, 0)
