class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max([nums[i] + nums[n - 1 - i] for i in range(n // 2)])
    
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        store = [0] * (10 ** 5 + 1)
        res = 0
        max_num, min_num = float('-inf'), float('inf')
        for num in nums:
            store[num] += 1
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        low, high = min_num, max_num

        while low <= high:
            if store[low] == 0:
                low += 1
            elif store[high] == 0:
                high -= 1
            else:
                res = max(res, low + high)
                store[low] -= 1
                store[high] -= 1
        return res