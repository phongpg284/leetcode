# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        n = 0

        if not head or k == 0:
            return head
        
        while cur.next:
            n += 1
            cur = cur.next
        n += 1
        
        if k % n == 0:
            return head
        
        k = k % n

        temp = head
        for _ in range(n - k - 1):
            temp = temp.next
        
        start = temp.next
        cur.next = head
        temp.next = None

        return start