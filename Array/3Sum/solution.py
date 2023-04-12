class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        map = dict()
        result = set()
        for index, item in enumerate(nums):
            map[item] = index

        len_list = len(nums)

        for i in range(0, len_list - 1):
            for j in range(i + 1, len_list):
                sum = -(nums[i] + nums[j])
                if sum in map and map[sum] > j:
                    new_item = (nums[i], nums[j], sum)
                    if (new_item in result) is False:
                        result.add(new_item)

        return result