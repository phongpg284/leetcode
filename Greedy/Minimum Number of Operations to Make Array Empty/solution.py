class Solution:
    def minOperations(self, nums: List[int]) -> int:
        store = Counter(nums)
        res = 0

        for count in store.values():
            if count == 1:
                return -1
            res += (count + 2) // 3

        return res
