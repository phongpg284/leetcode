# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = []
        prev, cur = head, head.next
        index = 1
        min_dist = float('inf')
        while cur.next:
            if (prev.val < cur.val and cur.next.val < cur.val) or (prev.val > cur.val and cur.next.val > cur.val):
                if len(res) > 0:
                    min_dist = min(min_dist, index - res[-1])
                res.append(index)
            prev = cur
            cur = cur.next
            index += 1

        max_dist = -1
        min_dist = min_dist if min_dist != float("inf") else -1
        if len(res) >= 2:
            max_dist = res[-1] - res[0]

        return [min_dist, max_dist]
