class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = []
        total = 0
        cost_count = 0

        data = list(zip(nums, cost))
        data = sorted(data, key=lambda x: x[0])

        '''
            data is sort by nums after zip
            dp[i] is total cost sum from start to element index i
        '''
        for item in data:
            total += item[1]
            dp.append(total)
        
        for i in range(n):
            (num, cost) = data[i]
            cost_count += (num - data[0][0]) * cost
        res = cost_count

        for i in range(1, n):
            cost_count += (2 * dp[i-1] - total) * (data[i][0] - data[i-1][0])
            res = min(res, cost_count)

        return res