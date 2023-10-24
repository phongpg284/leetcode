# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        res = []
        q = deque([root])
        
        while q:
            max_temp = float('-inf')
            cur_level = len(q)
            for _ in range(cur_level):
                top = q.popleft()
                max_temp = max(max_temp, top.val)
                if top.left:
                    q.append(top.left) 
                if top.right:
                    q.append(top.right)
            res.append(max_temp)
        return res 