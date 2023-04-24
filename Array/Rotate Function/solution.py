class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = 0
        sum = 0
        for i, num in enumerate(nums): 
            sum += (i * num)
            total += num
        
        max = sum

        for num in nums:
            sum = sum - total + len(nums) * num
            if sum > max:
                max = sum
        return max 
        