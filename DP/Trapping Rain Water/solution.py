class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        len_height = len(height)

        # max index from position i to left and right
        left_max = [0] * (len_height + 1)
        right_max = [0] * (len_height + 1)
        right_max[len_height - 1] = len_height - 1
        
        for i in range(1, len_height):
            last_left_max = left_max[i - 1]
            if height[i] > height[last_left_max]:
                left_max[i] = i
            else:
                left_max[i] = last_left_max
            
            last_right_max = right_max[len_height - i] 
            if height[len_height - 1 - i] > height[last_right_max]:
                right_max[len_height - 1 - i] = len_height - 1 - i
            else:
                right_max[len_height - 1 - i] = last_right_max

        max_pos = left_max[len_height - 1]
        end = max_pos
        start = left_max[end - 1]

        # move pointer to next max position to the left
        while end > 0:
            for i in range(start + 1, end):
                result += (height[start] - height[i])
            end = start
            start = left_max[end - 1]
        
        start = max_pos
        end = right_max[start + 1]

        # move pointer to next max position to the right
        while start < len_height - 1:
            for i in range(start + 1, end):
                result += (height[end] - height[i])
            start = end
            end = right_max[start + 1]

        return result
