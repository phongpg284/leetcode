class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0 ] * n
        res = []
        for i in range(n):
            if self.dfs(visited, graph, i, res):
                res.append(i)
        return res

    def dfs(self, visited, graph, node, cycle):
        if visited[node] == 1:
            return True
        if visited[node] == -1:
            return False

        visited[node] = -1
        for next in graph[node]:
            if not self.dfs(visited, graph, next, cycle):
                return False
        visited[node] = 1
        return True
