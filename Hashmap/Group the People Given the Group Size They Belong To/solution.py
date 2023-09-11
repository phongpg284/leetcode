class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        map = defaultdict(list)
        res = []
        for i, size in enumerate(groupSizes):
            map[size].append(i)
            if len(map[size]) == size:
                res.append(map[size])
                map[size] = []
        return res