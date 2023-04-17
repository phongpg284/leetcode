class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mark = [False] * len(nums)
        return self.permulation_recursive([], mark, nums, []) 

    def permulation_recursive(self, result, mark, nums, res):
        if len(result) == len(nums):
            res.append(result)
            return res

        for i in range(len(mark)):
            if mark[i] == False:
                new_mark = mark.copy()
                new_mark[i] = True
                new_result = result[::] 
                new_result.append(nums[i])
                self.permulation_recursive(new_result, new_mark, nums, res)
        return res