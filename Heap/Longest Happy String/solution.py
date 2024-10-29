class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        res = []

        while heap:
            count1, c1 = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == c1:
                if not heap:
                    break

                count2, c2 = heapq.heappop(heap)
                res.append(c2)

                if count2 + 1 < 0:
                    heapq.heappush(heap, (count2 + 1, c2))
                heapq.heappush(heap, (count1, c1))
            else:
                res.append(c1)
                if count1 + 1 < 0:
                    heapq.heappush(heap, (count1 + 1, c1))

        return ''.join(res)
