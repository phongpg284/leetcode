class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[1], succProb[i]))
            graph[edge[1]].append((edge[0], succProb[i]))

        dp = [0] * n
        dp[start] = 1

        queue = deque([start])
    
        while queue:
            cur = queue.popleft()

            for node, success in graph[cur]:
                new_success = dp[cur] * success

                if new_success > dp[node]:
                    dp[node] = new_success
                    queue.append(node)

        return dp[end] 