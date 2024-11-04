# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.recur(root1, root2)

    def recur(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2 or node1.val != node2.val:
            return False

        return (self.recur(node1.left, node2.left) or self.recur(node1.left, node2.right)) and (self.recur(node1.right, node2.right) or self.recur(node1.right, node2.left))
