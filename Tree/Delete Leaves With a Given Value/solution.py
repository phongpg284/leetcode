# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not self.valid(root, target):
            return None

        return root

    def valid(self, node, target):
        if not node.left and not node.right and node.val == target:
            return False

        left_check, right_check = None, None
        if node.left:
            left_check = self.valid(node.left, target)
            if not left_check:
                node.left = None
        if node.right:
            right_check = self.valid(node.right, target)
            if not right_check:
                node.right = None

        if not left_check and not right_check:
            if node.val == target:
                return False
        return True
