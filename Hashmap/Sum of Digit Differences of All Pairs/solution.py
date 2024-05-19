class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        digit_len = len(str(nums[0]))
        res = 0
        for i in range(digit_len):
            digits = [num % (10 ** (i + 1)) // (10 ** i) for num in nums]
            res += self.diff(digits)

        return res

    def diff(self, digits):
        res = 0
        count = Counter(digits)
        items = list(count.items())
        n = len(items)

        for i in range(n):
            for j in range(i + 1, n):
                res += items[i][1] * \
                    items[j][1] if items[i][0] != items[j][0] else 0

        return res
