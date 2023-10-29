class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie
        left, right = 0, buckets
        while left < right:
            mid = (left + right) // 2
            if (t + 1) ** mid >= buckets:
                right = mid
            else:
                left = mid + 1
        return left
    
# One line solution
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log2(buckets)/log2(minutesToTest//minutesToDie+1))