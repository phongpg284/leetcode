# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.helper(root, res)
        return res[0]

    def helper(self, node, res):
        if not node:
            return 0

        left = self.helper(node.left, res)
        right = self.helper(node.right, res)

        res[0] = max(res[0], left + right)

        return max(left, right) + 1
