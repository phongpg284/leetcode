class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low, high = 1, int(1e7)
        min_speed = -1
        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(dist, mid, hour):
                min_speed = mid
                high = mid - 1
            else:
                low = mid + 1
        return min_speed

    def isPossible(self, dist, speed, hour):
        ans = 0
        n = len(dist)
        for i in range(n - 1):
            ans += (dist[i] + speed - 1) // speed
            if ans > hour:
                return False
        ans += dist[n - 1] / speed
        return ans <= hour