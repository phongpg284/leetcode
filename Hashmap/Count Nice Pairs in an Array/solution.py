class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        res = 0
        store = defaultdict(int)

        for num in nums:
            rev_val = self.get_rev_val(num)
            res += store[rev_val]
            store[rev_val] += 1

        return res % mod

        
    def get_rev_val(self, num):
        s = str(num)
        return num - int(s[::-1])