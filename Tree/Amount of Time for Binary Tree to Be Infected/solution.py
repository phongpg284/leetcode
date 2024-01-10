# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        self.helper(root, graph)

        visited = set()
        visited.add(start)
        q = deque([start])

        infect = -1
        while q:
            infect += 1
            for _ in range(len(q)):
                top = q.popleft()
                for neighbor in graph[top]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        return infect

    def helper(self, node, graph):
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            self.helper(node.left, graph)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            self.helper(node.right, graph)
