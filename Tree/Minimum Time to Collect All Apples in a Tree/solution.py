class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = [False] * n

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        return max(self.get_steps(0, graph, hasApple, visited), 0)

    def get_steps(self, node, graph, hasApple, visited):
        visited[node] = True
        total = 0

        for child in graph[node]:
            if not visited[child]:
                child_steps = self.get_steps(child, graph, hasApple, visited)
                if child_steps > -1:
                    total += 2 + child_steps

        if not hasApple[node] and not total:
            return -1

        return total
