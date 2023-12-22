class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = nums[0]
        nums[0] *= 2
        
        for i in range(1, n):
            temp = max(temp, nums[i])
            nums[i] = nums[i - 1] + nums[i] + temp
        return nums