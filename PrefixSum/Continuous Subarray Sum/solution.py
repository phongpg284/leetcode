class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = {0: -1}
        count = 0
        for i, num in enumerate(nums):
            count += num
            temp = count % k

            if temp in store:
                if i - store[temp] >= 2:
                    return True
            else:
                store[temp] = i
        return False
