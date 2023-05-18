class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        root = [True] * n
        result = []
        for edge in edges:
            root[edge[1]] = False
        for i in range(n):
            if root[i]:
                result.append(i)
        return result
