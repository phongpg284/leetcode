class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        self.solve(nums, n, res, [], 0)
        return res

    def solve(self, nums, n, res, arr, i):
        new_arr = arr[::]
        res.append(new_arr)
        
        for j in range(i, n):
            arr.append(nums[j])
            self.solve(nums, n , res, arr, j + 1)
            arr.pop()