class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        store = {}
        res = []

        for num in nums:
            if num in store:
                store[num] = 2
            else:
                store[num] = 1
        
        for key in store.keys():
            if store[key] == 1 and key + 1 not in store and key - 1 not in store:
                res.append(key)

        return res