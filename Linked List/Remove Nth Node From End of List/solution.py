# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        store = list()
        current_node = head
        
        while current_node != None:
            store.append(current_node)
            current_node = current_node.next
        
        prev_node_index = len(store) - n - 1
        
        # delete first node
        if prev_node_index == -1:
            head = head.next
            return head

        prev_node = store[prev_node_index]
        prev_node.next = prev_node.next.next
        
        return head
