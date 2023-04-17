class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.permute_recur(nums, [], [])
    def permute_recur(self, nums, perm, result):
        if len(nums) == 0:
            result.append(perm[::])

        mark = set()
        for i in range(len(nums)):
            if (nums[i] in mark) is False:
                mark.add(nums[i])
                new_nums = nums[:i] + nums[i+1:]
                perm.append(nums[i])
                self.permute_recur(new_nums, perm, result)
                perm.pop()
        return result