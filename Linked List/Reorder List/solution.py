# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Finding the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide the linked list into two halves
        h2 = slow.next
        tail = slow.next = None

        # Reverse the second half of the linked list
        while h2:
            temp = h2.next
            h2.next = tail
            tail = h2
            h2 = temp

        # Merge two halves of the linked list
        h1, h2 = head, tail
        while h2:
            temp1, temp2 = h1.next, h2.next
            h1.next = h2
            h2.next = temp1
            h1, h2 = temp1, temp2
