class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        graph = defaultdict(list)
        for [course, require] in prerequisites:
            graph[require].append(course)

        for i in range(numCourses):
            if not visited[i]:
                if not self.checkCycle(graph, visited, i):
                    return False
        return True
    
    def checkCycle(self, graph, visited, node):
        if visited[node] == 1:
            return True
        if visited[node] == -1:
            return False

        visited[node] = -1
        
        for course in graph[node]:
            if not self.checkCycle(graph, visited, course):
                return False
        
        visited[node] = 1
        return True
