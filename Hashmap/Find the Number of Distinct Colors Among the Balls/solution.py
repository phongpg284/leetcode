class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        store = dict()
        color = defaultdict(int)
        count = 0
        for i, [x, y] in enumerate(queries):
            if x in store:
                if store[x] != y:
                    old_color = store[x]
                    color[old_color] -= 1
                    if color[old_color] == 0:
                        count -= 1

                    store[x] = y
                    color[y] += 1
                    if color[y] == 1:
                        count += 1
            else:
                store[x] = y
                color[y] += 1
                if color[y] == 1:
                    count += 1
            res[i] = count
        return res
