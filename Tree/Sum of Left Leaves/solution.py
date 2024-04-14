# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.helper(root, 0, res)
        return res[0]

    def helper(self, node, order, res):
        if order == -1 and not node.left and not node.right:
            res[0] += node.val

        if node.left:
            self.helper(node.left, -1, res)
        if node.right:
            self.helper(node.right, 1, res)
