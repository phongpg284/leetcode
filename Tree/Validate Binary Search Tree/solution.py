# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, cur, low, high):
        left, right = True, True
        t_low, t_high = low, high
        if cur.left:
            if cur.left.val >= cur.val:
                return False
            if low and cur.left.val <= low:
                return False

            t_high = min(t_high, cur.val)
            if cur.left.val >= high:
                return False

            left = self.helper(cur.left, t_low, t_high)

        t_low, t_high = low, high
        if cur.right:
            if cur.right.val <= cur.val:
                return False
            if high and cur.right.val >= high:
                return False

            t_low = max(t_low, cur.val)
            if cur.right.val <= low:
                return False

            right = self.helper(cur.right, t_low, t_high)

        return left and right
