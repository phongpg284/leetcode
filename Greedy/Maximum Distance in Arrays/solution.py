class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_dist = 0

        for i in range(1, n):
            arr = arrays[i]
            max_dist = max(max_dist, abs(
                arr[-1] - min_val), abs(max_val - arr[0]))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])

        return max_dist
