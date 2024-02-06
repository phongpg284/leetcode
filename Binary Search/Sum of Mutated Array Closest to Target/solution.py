class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        low = 0
        high = max(arr)
        t = float('inf')
        res = 0

        while low <= high:
            mid = (low + high) // 2
            total = sum([num if mid >= num else mid for num in arr])
            if total == target:
                return mid
            if abs(total - target) < t:
                res = mid
                t = abs(total - target)
            if total > target:
                high = mid - 1
            else:
                low = mid + 1

        if abs(total - target) == t:
            return min(mid, res)

        return mid if abs(total - target) < t else res
