class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.dfs(nums, 0, 0)

    def dfs(self, nums, i, cur):
        if i == len(nums):
            return cur
        include = self.dfs(nums, i + 1, cur ^ nums[i])
        exclude = self.dfs(nums, i + 1, cur)
        return include + exclude
