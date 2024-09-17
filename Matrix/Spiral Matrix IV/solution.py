# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        top, bot, left, right = 0, m - 1, 0, n - 1

        while head:
            for i in range(left, right + 1):
                if not head:
                    break
                matrix[top][i] = head.val
                head = head.next
            top += 1

            for i in range(top, bot + 1):
                if not head:
                    break
                matrix[i][right] = head.val
                head = head.next
            right -= 1

            for i in range(right, left - 1, -1):
                if not head:
                    break
                matrix[bot][i] = head.val
                head = head.next
            bot -= 1

            for i in range(bot, top - 1, -1):
                if not head:
                    break
                matrix[i][left] = head.val
                head = head.next
            left += 1

        return matrix
