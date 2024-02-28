# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([(0, root)])
        res = (0, root.val)
        while q:
            level, node = q.popleft()
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))

            if level > res[0]:
                res = (level, node.val)

        return res[1]
