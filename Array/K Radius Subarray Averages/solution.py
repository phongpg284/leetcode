class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        temp = 0

        if k == 0:
            return nums
        
        if k * 2 >= n:
            return res
        
        # Traverse first k-radius
        for i in range(k * 2 + 1):
            temp += nums[i]
        res[k] = int(temp / (2*k + 1) * 10 // 10)
        
        # Shift k-radius to the end
        for i in range(k + 1, n - k):
            temp += nums[i+k] - nums[i-k-1]
            res[i] = int(temp / (2*k + 1) * 10 // 10)
        return res    
