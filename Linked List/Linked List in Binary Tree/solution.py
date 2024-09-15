# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.dfs(root, head)

    def is_valid(self, root, head):
        if not head:
            return True
        if not root or head.val != root.val:
            return False

        return self.is_valid(root.left, head.next) or self.is_valid(root.right, head.next)

    def dfs(self, node, cur):
        if not node:
            return False

        if self.is_valid(node, cur):
            return True

        return self.dfs(node.left, cur) or self.dfs(node.right, cur)
