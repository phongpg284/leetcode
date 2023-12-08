# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ['']
        self.preorder_traversal(root, res)
        return res[0]
    def preorder_traversal(self, node, res):
        res[0] += str(node.val)
        
        if not node.left and not node.right:
            return

        res[0] += '('
        if node.left:
            self.preorder_traversal(node.left, res)
        res[0] += ')'
        
        if node.right:
            res[0] += '('
            self.preorder_traversal(node.right, res)
            res[0] += ')'
        