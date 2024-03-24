class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        mark = [False] * (n + 1)
        for num in nums:
            if mark[num]:
                return num
            else:
                mark[num] = True


# Hare & Tortoise 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast