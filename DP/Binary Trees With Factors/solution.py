class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        arr = sorted(arr) 
        dp = [-1] * n
        map = dict()
        for i in range(n):
            map[arr[i]] = i
        res = 0
        def factored_binary_trees(index):
            if dp[index] > -1:
                return dp[index]
            temp = 1
            cur = arr[index]
            for i in range(index):
                product = cur // arr[i]
                if cur % arr[i] == 0 and product in map:
                    temp += (factored_binary_trees(i) * factored_binary_trees(map[product]))
            dp[index] = temp % mod
            return dp[index]

        for i in range(n):
            res = (res + factored_binary_trees(i))

        return res % mod