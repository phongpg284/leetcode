class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        left_max = [0] * (n + 1)
        right_max = [0] * (n + 1)
        right_max[n - 1] = n - 1
        for i in range(1, n):
            last_left_max = left_max[i - 1]
            if height[i] > height[last_left_max]:
                left_max[i] = i
            else:
                left_max[i] = last_left_max

            last_right_max = right_max[n - i]
            if height[n - 1 - i] > height[last_right_max]:
                right_max[n - 1 - i] = n - 1 - i
            else:
                right_max[n - 1 - i] = last_right_max

        max_pos = left_max[n - 1]
        end = max_pos
        start = left_max[end - 1]

        while end > 0:
            for i in range(start + 1, end):
                result += (height[start] - height[i])
            end = start
            start = left_max[end - 1]

        start = max_pos
        end = right_max[start + 1]

        while start < n - 1:
            for i in range(start + 1, end):
                result += (height[end] - height[i])
            start = end
            end = right_max[start + 1]

        return result
