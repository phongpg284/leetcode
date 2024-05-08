class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [0] * n
        place = 1

        heap = []
        for i, score in enumerate(score):
            heapq.heappush(heap, (-score, i))

        while heap:
            index = heapq.heappop(heap)[1]
            if place == 1:
                res[index] = "Gold Medal"
            elif place == 2:
                res[index] = "Silver Medal"
            elif place == 3:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(place)
            place += 1

        return res
