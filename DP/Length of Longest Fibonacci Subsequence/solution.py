class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        store = set()
        res = 0
        for i, num in enumerate(arr):
            store.add(num)
            t = 1
            ind = bisect_left(arr, num // 2)
            for j in range(ind, i):
                t = max(t, self.helper(arr[j], num, store))
            res = max(res, t)
        return res if res > 2 else 0

    def helper(self, a, b, store):
        prev = b - a
        if prev != a and prev < a and prev in store:
            return self.helper(prev, a, store) + 1
        return 2
