# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1

        for _ in range(a - 1):
            start = start.next
        end = start.next
        start.next = list2

        for _ in range(a, b + 1):
            end = end.next

        while list2.next:
            list2 = list2.next
        list2.next = end

        return list1
