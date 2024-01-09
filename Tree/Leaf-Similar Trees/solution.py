# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        self.helper(root1, leaf1)
        self.helper(root2, leaf2)
        return leaf1 == leaf2

    def helper(self, node, leaf):
        if node.left:
            self.helper(node.left, leaf)
        if node.right:
            self.helper(node.right, leaf)

        if node.left is None and node.right is None:
            leaf.append(node.val)
