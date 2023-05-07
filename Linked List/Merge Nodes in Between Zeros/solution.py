# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node.next != None:
            next = node.next
            if next.val == 0:
                if next.next == None:
                    node.next = None
                    break
                node = next
            else:
                node.val += next.val
                node.next = next.next

        return head
        

