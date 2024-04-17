# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        queue = deque([root])
        level = 1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if level == depth - 1:
                    new_left = TreeNode(val, node.left, None)
                    node.left = new_left

                    new_right = TreeNode(val, None, node.right)
                    node.right = new_right
            level += 1
            if level >= depth:
                return root
