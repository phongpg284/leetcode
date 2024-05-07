# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        residual = self.helper(head)
        if residual > 0:
            head = ListNode(residual, head)
        return head

    def helper(self, node):
        if not node:
            return 0

        temp = node.val * 2 + self.helper(node.next)
        node.val = temp % 10
        return temp // 10
