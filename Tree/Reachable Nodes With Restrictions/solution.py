class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = 1
        graph = defaultdict(list)
        visited = [False] * n
        restricted = set(restricted)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([0])
        while q:
            node = q.popleft()
            visited[node] = True

            for child in graph[node]:
                if not visited[child]:
                    if child not in restricted:
                        res += 1
                        q.append(child)

        return res
