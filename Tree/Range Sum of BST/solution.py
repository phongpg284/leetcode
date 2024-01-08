# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0]
        self.helper(root, res, low, high)
        return res[0]

    def helper(self, node, res, low, high):
        if node.val >= low and node.val <= high:
            res[0] += node.val

        if node.left and node.val >= low:
            self.helper(node.left, res, low, high)
        if node.right and node.val <= high:
            self.helper(node.right, res, low, high)
