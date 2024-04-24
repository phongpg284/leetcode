class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque([])
        for node, child in graph.items():
            if len(child) == 1:
                q.append(node)

        while n > 2:
            n -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in graph[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        q.append(neighbor)
        return list(q)
