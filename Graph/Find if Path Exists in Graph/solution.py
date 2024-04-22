class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])
        visited[source] = True

        while q:
            node = q.pop()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True

        return False
