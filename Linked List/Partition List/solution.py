# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        low, high, high_head = None, None, None
        while cur:
            if cur.val >= x:
                if not high:
                    high = cur
                    high_head = cur
                else:
                    high.next = cur
                    high = high.next
            else:
                if not low:
                    low = cur
                    head = cur
                else:
                    low.next = cur
                    low = low.next
            cur = cur.next
        if high:
            high.next = None
        if low:
            low.next = high_head
        
        return head