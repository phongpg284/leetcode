class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i + 1 for i in range(m)]
        res = []

        for q in queries:
            i = arr.index(q)
            res.append(i)
            arr = [q] + arr[:i] + arr[i + 1:]

        return res
