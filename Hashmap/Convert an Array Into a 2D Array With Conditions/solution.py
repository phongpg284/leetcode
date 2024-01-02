class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        store = {}

        for num in nums:
            if num not in store:
                store[num] = 0
            store[num] += 1

        for num in store.keys():
            count = store[num]
            for i in range(count):
                if i >= len(res):
                    res.append([])
                res[i].append(num)
        return res
