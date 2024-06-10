class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)

        t = 0
        for num in nums:
            t += num
            store[t % k] += 1

        res = 0
        for i in range(k):
            res += store[i] * (store[i] - 1) // 2

        return res + store[0]
