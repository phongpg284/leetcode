# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        temp = []
        result = 0
        n = 0
        while cur:
            temp.append(cur.val)
            n += 1
            cur = cur.next
        
        for i in range(n // 2):
            result = max(result, temp[i] + temp[n - 1 - i])
        return result


        
