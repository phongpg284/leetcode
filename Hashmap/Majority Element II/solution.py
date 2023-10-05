class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = defaultdict(int)
        res = set()
        for num in nums:
            dp[num] += 1
            if dp[num] > n // 3:
                res.add(num)
        return list(res)
    