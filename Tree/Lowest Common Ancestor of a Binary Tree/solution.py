# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [None]
        self.helper(root, p, q, res)
        return res[0]

    def helper(self, node, p, q, res):
        left_check, right_check = None, None
        if node.left:
            left_check = self.helper(node.left, p, q, res)
        if node.right:
            right_check = self.helper(node.right, p, q, res)

        if node == p or node == q:
            if left_check or right_check:
                res[0] = node
            return True

        if left_check and right_check:
            res[0] = node
            return True

        if left_check or right_check:
            return True
        return False
