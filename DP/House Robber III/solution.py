# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        pick, not_pick = self.helper(root)
        return max(pick, not_pick)

    def helper(self, node):
        pick = node.val
        not_pick = 0

        if node.left:
            left_pick, left_not_pick = self.helper(node.left)
            pick += left_not_pick
            not_pick += max(left_pick, left_not_pick)

        if node.right:
            right_pick, right_not_pick = self.helper(node.right)
            pick += right_not_pick
            not_pick += max(right_pick, right_not_pick)
        return pick, not_pick
