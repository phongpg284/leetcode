class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        count = 1
        pos = {}
        for i, num in enumerate(nums):
            if num == x:
                pos[count] = i
                count += 1

        res = [-1] * len(queries)

        for i, q in enumerate(queries):
            if q in pos:
                res[i] = pos[q]
        return res
