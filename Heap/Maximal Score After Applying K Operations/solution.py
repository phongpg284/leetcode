class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0

        for i in range(k):
            num = -heapq.heappop(nums)
            res += num
            if num == 1:
                res += k - 1 - i
                break
            heapq.heappush(nums, -((num + 2) // 3))

        return res
