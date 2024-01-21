# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([(root, 0)])
        res = []
        while q:
            node, level = q.popleft()

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

            if len(q) == 0 or q[0][1] == level + 1:
                res.append(node.val)

        return res
