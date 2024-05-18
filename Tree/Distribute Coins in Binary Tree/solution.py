# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.check(root, res)
        return res[0]

    def check(self, node, res):
        if not node:
            return 0

        left_check = self.check(node.left, res)
        right_check = self.check(node.right, res)

        node.val += left_check + right_check
        res[0] += abs(node.val - 1)
        return node.val - 1
