class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        for key, val in graph.items():
            if len(val) == 1:
                start = key
                break
        
        q = deque([start])
        res = []
        visited = set()
        
        while q:
            top = q.pop()
            visited.add(top)
            res.append(top)
            neighbors = graph[top]
            if neighbors:
                for neighbor in neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
        return res
        