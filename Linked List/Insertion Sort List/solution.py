# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        while head:
            temp = dummy
            while True:
                if temp.next and temp.next.val < head.val:
                    temp = temp.next
                else:
                    copy_head = head
                    head = head.next
                    copy_head.next = temp.next
                    temp.next = copy_head
                    break
        return dummy.next
