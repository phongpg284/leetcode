class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        for i in range(n):
            self.dfs(i, i, graph, [False] * n, res)

        return res

    def dfs(self, cur, ancestor, graph, visited, res):
        visited[cur] = True

        for child in graph[cur]:
            if not visited[child]:
                res[child].append(ancestor)
                self.dfs(child, ancestor, graph, visited, res)
