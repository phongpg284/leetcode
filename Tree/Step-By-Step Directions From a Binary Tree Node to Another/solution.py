# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path_start = []
        path_end = []
        self.findPath(root, startValue, path_start)
        self.findPath(root, destValue, path_end)

        while path_start and path_end and path_start[-1] == path_end[-1]:
            path_start.pop()
            path_end.pop()

        return "".join(["U"] * len(path_start) + path_end[::-1])

    def findPath(self, node, target, path):
        if node.val == target:
            return True
        if node.left and self.findPath(node.left, target, path):
            path += 'L'
        elif node.right and self.findPath(node.right, target, path):
            path += 'R'
        return path
