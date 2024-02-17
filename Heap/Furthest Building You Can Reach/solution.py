class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        s = []
        for i in range(n - 1):
            dif = heights[i + 1] - heights[i]
            while dif > 0:
                if bricks >= dif:
                    bricks -= dif
                    heapq.heappush(s, -dif)
                    dif = 0
                else:
                    if ladders == 0:
                        return i

                    if len(s) > 0:
                        top = s[0]
                        if dif > -top:
                            dif = 0
                        else:
                            heapq.heappop(s)
                            bricks -= top
                    else:
                        dif = 0
                    ladders -= 1
        return n - 1
