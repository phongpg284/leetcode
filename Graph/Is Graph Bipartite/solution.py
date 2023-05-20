# Recursive
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool: 
        prev_visited = [0] * len(graph)
        for i in range(len(graph)):
            if prev_visited[i] == 0:
                visited = [0] * len(graph)
                result = self.dfs(graph, i, visited, 1)
                if result is False:
                    return False
                prev_visited = visited
        return True

    def dfs(self, graph, vertex, visited, count):
        # mark node traverse visited
        visited[vertex] = count
        for neighbor in graph[vertex]:
            # check if cycle appear
            if visited[neighbor] > 0:
                cycle_length = count - visited[neighbor] + 1
                # if cycle_length is odd and > 1, this will not be bipartite graph
                if cycle_length > 1 and cycle_length % 2 == 1:
                    return False
            else:
                result = self.dfs(graph, neighbor, visited, count + 1)
                if result is False:
                    return False
                return True
        return True
