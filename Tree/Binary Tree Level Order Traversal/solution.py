# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [(root, 0)]
        result = []
        temp = []
        level = 0
        while (len(queue) > 0):
            curr = queue.pop(0)
            if curr[1] > level:
                result.append(temp)
                temp = []
                level += 1
            temp.append(curr[0].val)
            if curr[0].left != None:
                queue.append((curr[0].left, curr[1] + 1))
            if curr[0].right != None:
                queue.append((curr[0].right, curr[1] + 1))
        result.append(temp)
        return result