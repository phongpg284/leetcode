class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [0]
        for i in range(n):
            dp += [num + (1 << i) for num in dp[::-1]]
        return dp
