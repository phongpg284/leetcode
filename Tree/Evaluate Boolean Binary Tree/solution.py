# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.evaluate(root)

    def evaluate(self, node):
        if node.val <= 1:
            return node.val == 1

        v_left = self.evaluate(node.left)
        v_right = self.evaluate(node.right)

        if node.val == 2:
            return v_left or v_right
        return v_left and v_right
