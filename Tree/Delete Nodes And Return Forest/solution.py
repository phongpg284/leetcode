# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = {root.val: root}
        self.dfs(None, root, False, to_delete, res)

        return res.values()

    def dfs(self, parent, node, is_left, to_delete, res):
        if node is None:
            return

        self.dfs(node, node.left, True, to_delete, res)
        self.dfs(node, node.right, False, to_delete, res)

        if node.val in to_delete:
            if node.val in res:
                del res[node.val]

            if parent:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None

            if node.left:
                res[node.left.val] = node.left
            if node.right:
                res[node.right.val] = node.right
