# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dp = []
        
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            child_sum = 0
            if node.left:
                q.append((node.left, level + 1))
                child_sum += node.left.val
            if node.right:
                q.append((node.right, level + 1))
                child_sum += node.right.val
            
            if len(dp) < level + 1:
                dp.append(0)

            dp[level] += node.val
        
        q.append((root, 0, root.val))
        while q:
            node, level, child_sum = q.popleft()
            temp = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            if node.left:
                q.append((node.left, level + 1, temp))
            if node.right:
                q.append((node.right, level + 1, temp))
            
            node.val = dp[level] - child_sum
        
        return root

