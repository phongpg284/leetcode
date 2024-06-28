# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorder(root, arr)
        return self.sortedArrToBST(arr, 0, len(arr) - 1)

    def inorder(self, node, arr):
        if not node:
            return
        self.inorder(node.left, arr)
        arr.append(node)
        self.inorder(node.right, arr)

    def sortedArrToBST(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = arr[mid]
        root.left = self.sortedArrToBST(arr, start, mid - 1)
        root.right = self.sortedArrToBST(arr, mid + 1, end)
        return root
