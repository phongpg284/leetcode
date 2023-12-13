class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        res = [False] * n
        p = dict()
        dp = [[-1] * n for _ in range(n)]
 
        for x, y in pairs:
            p[x] = y
            p[y] = x

        for i, preference in enumerate(preferences):
            for index, j in enumerate(preference):
                dp[i][j] = index 
        
        for x in range(n):
            y = p[x]
            preference = preferences[x]
            y_rank = dp[x][y]

            for i in range(y_rank):
                u = preference[i]
                if res[x] == 1 and res[u] == 1:
                    continue
                v = p[u]
                if dp[x][u] < dp[x][y] and dp[u][x] < dp[u][v]:
                    res[x] = True
                    res[u] = True
        return sum(res)