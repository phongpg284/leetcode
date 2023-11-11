class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        
        for i in range(n):
            self.solve(nums, n, res, [], i)
        return res

    def solve(self, nums, n, res, arr, i):
        if i == n:
            res.append(arr)
            return

        arr.append(nums[i])
        
        for j in range(i + 1, n + 1):
            new_arr = arr[::] 
            self.solve(nums, n , res, new_arr, j)