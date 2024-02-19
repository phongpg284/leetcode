# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.helper(root, res, k)
        return res[-1]

    def helper(self, node, res, k):
        if node.left:
            self.helper(node.left, res, k)

        if len(res) == k:
            return

        res.append(node.val)

        if node.right:
            self.helper(node.right, res, k)
