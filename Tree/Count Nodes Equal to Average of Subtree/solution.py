# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.dfs(root, res)
        return res[0]
    def dfs(self, node, res):
        count = 1
        sum = node.val
        if node.left:
            c, s = self.dfs(node.left, res)
            count += c
            sum += s
        if node.right:
            c, s = self.dfs(node.right, res)
            count += c
            sum += s
        if node.val == sum // count:
            res[0] += 1
        return count, sum