# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, p, q):
        if p is None or q is None:
            return p == q
        return p.val == q.val and self.helper(p.left, q.right) and self.helper(p.right, q.left)
