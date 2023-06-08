class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low = 1
        high = maxSum
        while low <= high:
            mid = (low + high) // 2
            cur = self.getSum(mid, n, index)
            next = self.getSum(mid + 1, n, index)
            if cur <= maxSum and next > maxSum:
                return mid
            elif cur > maxSum:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
    def getSum(self, A, n, index):
        s = n - index - 1
        total = 0
        if A > index:
            total += (A - 1 + A - index) * index / 2
        else:
            total += A * (A - 1) / 2 + (index - A + 1)
        
        if A > s:
            total += (A - 1 + A - s) * s / 2
        else:
            total += A * (A - 1) / 2 + (s - A + 1)
        
        return total + A