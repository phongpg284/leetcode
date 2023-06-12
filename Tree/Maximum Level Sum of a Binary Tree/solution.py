# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack = [(root,1)]
        temp = 0
        level = 1
        res = 0
        max_sum = float('-inf')
        while len(stack) != 0:
            (item, lv) = stack.pop(0)
            if lv != level:
                if temp > max_sum:
                    res = level
                    max_sum = temp
                temp = 0
                level += 1
            temp += item.val
            if item.left:
                stack.append((item.left, level + 1))
            if item.right:
                stack.append((item.right, level + 1))
        if temp > max_sum:
            res = level
            max_sum = temp
        return res
