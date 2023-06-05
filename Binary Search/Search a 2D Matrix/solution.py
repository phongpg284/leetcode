class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1
        while low <= high:
            middle = (low + high) // 2
            row = middle // n
            col = middle - row * n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = middle - 1
            else:
                low = middle + 1
        return False
