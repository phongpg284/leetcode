class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # dp[i][j] represents maximum dot product from i in nums1 and j in nums2
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                # whether take current product i, j or not
                dp[i][j] = max(dp[i][j], curr_product, dp[i-1][j], dp[i][j-1], curr_product + dp[i-1][j-1])
        
        return dp[m][n]
    
# Optimize by only store 2 state prev and current dp
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        current = [float('-inf')] * (n + 1)
        previous = [float('-inf')] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                
                current[j] = max(curr_product, previous[j], current[j-1], curr_product + max(0, previous[j-1]))
            
            current, previous = previous, current
        
        return previous[n]