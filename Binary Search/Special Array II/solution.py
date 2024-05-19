class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        fail = []
        i = 0
        n = len(queries)
        res = [False] * n

        while i + 1 < len(nums):
            if (nums[i] + nums[i + 1]) % 2 == 0:
                fail.append(i)
            i += 1

        for i, [start, end] in enumerate(queries):
            start_index = bisect_left(fail, start)
            end_index = bisect_left(fail, end)
            if start_index == end_index:
                res[i] = True
        return res
