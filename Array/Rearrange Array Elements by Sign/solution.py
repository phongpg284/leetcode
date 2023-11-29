class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive = []
        negative = []
        res = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        
        for i in range(n // 2):
            res.append(positive[i])
            res.append(negative[i])
        
        return res