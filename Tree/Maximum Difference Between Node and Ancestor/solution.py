# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        low = high = node.val
        if node.left:
            low_left, high_left = self.dfs(node.left)
            low = min(low, low_left)
            high = max(high, high_left)
        if node.right:
            low_right, high_right = self.dfs(node.right)
            low = min(low, low_right)
            high = max(high, high_right)
        self.res = max(self.res, abs(node.val - low), abs(node.val - high))
        return low, high
