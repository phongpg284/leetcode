import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
            - init 2 heap represents from left side and right side
            - start, end represents index of last item in each heap
        '''
        res = 0
        start, end = 0, len(costs) - 1
        left, right = [], []
        while k > 0:
            while len(left) < candidates and start <= end:
                heapq.heappush(left, costs[start])
                start += 1
            while len(right) < candidates and start <= end:
                heapq.heappush(right, costs[end])
                end -= 1

            temp_left = left[0] if left else float('inf')
            temp_right = right[0] if right else float('inf')

            if temp_left <= temp_right:
                res += temp_left
                heapq.heappop(left)
            else:
                res += temp_right
                heapq.heappop(right)
            
            k -= 1
        return res 
