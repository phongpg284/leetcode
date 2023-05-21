from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        graph = dict()
        result = []
        count = 0
        for i, [a, b] in enumerate(equations):
            edges[a].append((b, values[i]))
            edges[b].append((a, 1/values[i]))
            graph[a] = (-1, -1)
            graph[b] = (-1, -1)
            
        for i in graph.keys():
            if graph[i][0] == -1:
                count += 1
                self.dfs(edges, i, graph, 1, count)

        for [a, b] in queries:
            if a not in graph or b not in graph or graph[a][1] != graph[b][1]:
                result.append(-1)
            else:
                result.append(graph[a][0] / graph[b][0])
        return result

    def dfs(self, edges, vertex, graph, value, count):
        graph[vertex] = (value, count)
        for neighbor in edges[vertex]:
            if graph[neighbor[0]][0] == -1:
                self.dfs(edges, neighbor[0], graph, value/neighbor[1], count)

