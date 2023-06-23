class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # Mark the last index of num == 1
        last_index = -1
        res = 1
        for i, num in enumerate(nums):
            if num == 1:
                if last_index > -1:
                    res = res * (i - last_index)    
                last_index = i
        if last_index == -1:
            return 0
        
        '''
            Result will be multiply of zeros different between 2 consecutive ones
        '''
        return res % (10 ** 9 + 7)
        