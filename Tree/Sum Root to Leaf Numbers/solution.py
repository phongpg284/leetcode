# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.helper(root, '', res)
        return res[0]

    def helper(self, node, val, res):
        val += str(node.val)
        if not node.left and not node.right:
            res[0] += int(val)

        if node.left:
            self.helper(node.left, val, res)

        if node.right:
            self.helper(node.right, val, res)
