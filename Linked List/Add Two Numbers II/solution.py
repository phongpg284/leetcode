# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = []
        second = []
        cur = l1
        while cur:
            first.append(cur)
            cur = cur.next
        
        cur = l2
        while cur:
            second.append(cur)
            cur = cur.next
        
        if len(first) <= len(second):
            low = first[::-1] 
            high = second[::-1]
        else:
            high = first[::-1] 
            low = second[::-1]

        count = 0
        for i in range(len(high)):
            temp = 0
            if i < len(low):
                temp = low[i].val
            total = temp + high[i].val + count
            count = total // 10
            high[i].val = total % 10
        res = high[-1]
        if count > 0:
            res = ListNode(count, high[-1])
        return res
        