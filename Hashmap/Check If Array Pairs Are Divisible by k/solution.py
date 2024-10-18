class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        store = defaultdict(int)

        for num in arr:
            store[(num + k) % k] += 1

        for val in store.keys():
            if val != 0:
                if val == k / 2 and store[val] % 2 == 1:
                    return False

                if store[val] != store[k - val]:
                    return False

        return True
