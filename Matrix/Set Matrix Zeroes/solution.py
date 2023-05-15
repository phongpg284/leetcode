class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # if first row has 0
        is_row_zero = False
        # if first col has 0
        is_col_zero = False
        
        for i in range(n):
            if matrix[0][i] == 0:
                is_row_zero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                is_col_zero = True
                break

        # set corresponding row and col = 0 if matrix[i][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set matrix = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if is_row_zero:
            for i in range(n):
                matrix[0][i] = 0
        
        if is_col_zero:
            for i in range(m):
                matrix[i][0] = 0