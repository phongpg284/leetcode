# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        store = {}
        s = set()
        for parent, child, is_left in descriptions:
            s.add(child)

            if not parent in store:
                store[parent] = TreeNode(parent)
            if not child in store:
                store[child] = TreeNode(child)

            if is_left:
                store[parent].left = store[child]
            else:
                store[parent].right = store[child]

        for parent, _, _ in descriptions:
            if parent not in s:
                return store[parent]
