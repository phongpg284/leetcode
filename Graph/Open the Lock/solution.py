class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        n = len(deadends)
        visited = [False] * 10000
        for deadend in deadends:
            visited[int(deadend)] = True
        queue = deque(['0000'])
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return level
                if not visited[int(node)]:
                    visited[int(node)] = True
                    queue.extend(self.get_neighbors(node))
            level += 1
        return -1

    def get_neighbors(self, s):
        res = []
        for i, c in enumerate(s):
            res.append(s[:i] + str((int(c) + 1) % 10) + s[i + 1:])
            res.append(s[:i] + str((int(c) - 1) % 10) + s[i + 1:])
        return res
