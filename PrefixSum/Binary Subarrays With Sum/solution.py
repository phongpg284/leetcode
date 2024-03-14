class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        res = 0
        t = 0

        for num in nums:
            t += num
            if t - goal in count:
                res += count[t - goal]
            count[t] = count.get(t, 0) + 1

        return res


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        res = 0
        t = 0

        for num in nums:
            if num == 1:
                t += 1
                count[t] = 1
            else:
                count[t] += 1

        for num in count.keys():
            if goal == 0:
                res += count[num] * (count[num] - 1) // 2
            else:
                next = num + goal
                if next in count:
                    res += count[num] * count[next]
        return res
