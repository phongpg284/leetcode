# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        first = second = head
        count = 1
        while fast.next != None:
            if count < k:
                count += 1
                fast = fast.next
                first = fast
            else:
                slow = slow.next
                fast = fast.next
                second = slow
        first.val, second.val = second.val, first.val
        return head