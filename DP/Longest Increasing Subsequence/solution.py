class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    

# binary search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        res = 1

        for i in range(1, len(nums)):
            if temp[-1] < nums[i]:
                temp.append(nums[i])
                res += 1
            else:
                ind = bisect.bisect_left(temp, nums[i])
                temp[ind] = nums[i]

        return res
