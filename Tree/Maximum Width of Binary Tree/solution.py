# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        res = 0
        while q:
            min_idx = float('inf')
            max_idx = float('-inf')
            for _ in range(len(q)):
                node, val = q.popleft()
                min_idx = min(min_idx, val)
                max_idx = max(max_idx, val)
                if node.left:
                    q.append((node.left, val * 2))
                if node.right:
                    q.append((node.right, val * 2 + 1))

            res = max(res, max_idx - min_idx + 1)

        return res
