# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        prev = ListNode(0, head)
        current = head.next
        head = current
        count = 0
        while current != None:
            if count % 2 == 0:
                next = current.next
                temp = prev.next
                temp.next = next
                current.next = temp
                prev.next = current
                current = temp.next
            else:
                current = current.next
            
            prev = prev.next
            count += 1

        return head
