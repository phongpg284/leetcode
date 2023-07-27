class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low, high = 1, sum(batteries) // n
        m = len(batteries)

        while low < high:
            mid = (high + low + 1) // 2
            time = 0
            for battery in batteries:
                time += min(battery, mid) * m // n

            if mid * n <= time:
                low = mid
            else:
                high = mid - 1
        return low