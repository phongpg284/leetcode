class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 1

        for num in nums:
            if count == 0:
                return False
            count -= 1
            count = max(count, num)

        if count >= 0:
            return True