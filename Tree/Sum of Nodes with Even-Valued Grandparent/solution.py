# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]
        self.check(root, False, res)
        return res[0]

    def check(self, node, is_even_parent, res):
        if node.left:
            if is_even_parent:
                res[0] += node.left.val
            self.check(node.left, node.val % 2 == 0, res)
        if node.right:
            if is_even_parent:
                res[0] += node.right.val
            self.check(node.right, node.val % 2 == 0, res)
