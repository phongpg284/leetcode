class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)

        for prev, next in relations:
            graph[prev].append(next)
            in_degree[next] += 1

        dist = [0] + time
        q = deque([i for i in range(1, n+1) if in_degree[i] == 0])
        
        while q:
            course = q.popleft()
            for next_course in graph[course]:
                dist[next_course] = max(dist[next_course], dist[course] + time[next_course - 1])
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        return max(dist)
