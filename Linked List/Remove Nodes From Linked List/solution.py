# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        cur = head

        while cur:
            store.append(cur)
            cur = cur.next

        temp = -1
        valid_index = []
        for i in range(len(store) - 1, -1, -1):
            if store[i].val >= temp:
                temp = store[i].val
                valid_index.append(i)

        head = store[valid_index[-1]]
        cur = head
        i = len(valid_index) - 2
        while i >= 0:
            cur.next = store[valid_index[i]]
            cur = cur.next
            i -= 1
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        curr, prev.next = prev.next, None
        while curr:
            temp = curr.next
            if curr.val >= prev.val:
                curr.next = prev
                prev = curr
            curr = temp

        return prev
