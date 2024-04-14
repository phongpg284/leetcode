class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            res = max(res, self.max_area(heights))
        return res

    def max_area(self, heights):
        n = len(heights)
        res = 0
        stack = deque()

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)

        return res
