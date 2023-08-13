class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        def recur(index):
            if index == n:
                return True
            
            if dp[index] != 0:
                return True if dp[index] == 1 else False

            if n - index < 2:
                return False
            else: 
                if n - index == 2:
                    return nums[index] == nums[index + 1]
                else:
                    if nums[index] == nums[index + 1] and recur(index + 2):
                        dp[index] = 1
                        return True
                    if (nums[index] == nums[index + 1] == nums[index + 2] or nums[index] == nums[index + 1] - 1 == nums[index + 2] - 2) and recur(index + 3):
                        dp[index] = 1
                        return True
            dp[index] = -1
            return False
        return recur(0)
