class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = dict()
        for num in nums:
            if num not in store:
                store[num] = 1
            else:
                store[num] = store[num] + 1
        temp = sorted(store.items(), key=lambda item: item[1], reverse=True)
        return list(map(lambda x: x[0], temp[:k]))

