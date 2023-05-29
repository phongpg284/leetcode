class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            result = str(nums[0]) + "/"
            result += "(" + ("/").join(str(num) for num in nums[1:]) + ")"
        return result