class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        province = 0
        for i in range(n):
            if visited[i] is False:
                self.traverse(isConnected, visited, i)
                province += 1
        return province

    def traverse(self, isConnected, visited, node):
        visited[node] = True
        neighbors = isConnected[node]
        for i, relation in enumerate(neighbors):
            if relation == 1 and visited[i] is False:
                self.traverse(isConnected, visited, i) 
