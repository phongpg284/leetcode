# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = ["z" * 15]
        self.helper(root, [], res)
        return res[0]

    def helper(self, node, temp, res):
        temp.append(chr(node.val + ord('a')))

        if not node.left and not node.right:
            s = ''.join(temp[::-1])
            res[0] = min(res[0], s)

        if node.left:
            self.helper(node.left, temp, res)
        if node.right:
            self.helper(node.right, temp, res)

        temp.pop()
