# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None: 
            return head

        prev = ListNode(0, head)
        current = head
        count = 0
        queue = deque()
        while current != None:
            queue.append(current)
            if (count + 1) % k == 0: 
                current = current.next
                for i in range(k):
                    temp = queue.pop()
                    prev.next = temp
                    prev = prev.next
                    if count + 1 == k and i == 0:
                        head = temp
                prev.next = current
            else:
                current = current.next
            count += 1
        return head