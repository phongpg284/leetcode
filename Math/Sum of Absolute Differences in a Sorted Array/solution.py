# Prefix sum solution
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
            suffix[n - 1 - i] = suffix[n - i] + nums[n - 1 - i]
        
        for i in range(n):
            res[i] = (nums[i] * i - prefix[i]) + (suffix[i] - nums[i] * (n - i - 1))
        return res
    
# Slide window solution
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left, right = 0, total_sum
        result = []

        for i, n in enumerate(nums):
            right -= n
            result.append(n * i - left + right - n * (len(nums) - i - 1))
            left += n

        return result
               