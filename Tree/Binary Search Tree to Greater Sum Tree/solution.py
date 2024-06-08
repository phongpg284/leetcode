# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.greaterSum(root, 0)
        return root

    def greaterSum(self, node, greater_sum):
        old_val = node.val
        right_sum = self.greaterSum(
            node.right, greater_sum) if node.right else 0
        left_sum = self.greaterSum(
            node.left, greater_sum + node.val + right_sum) if node.left else 0

        node.val += greater_sum + right_sum
        return left_sum + right_sum + old_val
