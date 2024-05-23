class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = [0]
        visited = defaultdict(int)
        n = len(nums)
        self.helper(0, k, nums, res, visited)
        return res[0] - 1

    def helper(self, i, k, nums, res, visited):
        if i == len(nums):
            res[0] += 1
            return

        num = nums[i]
        
        if not visited[num - k] and not visited[num + k]:
            visited[num] += 1
            self.helper(i + 1, k, nums, res, visited)
            visited[num] -= 1

        self.helper(i + 1, k, nums, res, visited)
