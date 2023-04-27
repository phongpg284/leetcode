class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        row = []
        result = float('inf')
        for i in range(n):
            temp = []
            for j in range(i + 1):
                if i == 0:
                    temp.append(triangle[0][0])
                elif j == 0:
                    temp.append(row[j] + triangle[i][j])
                elif j == i:
                    temp.append(row[j-1] + triangle[i][j])
                else:
                    temp.append(min(row[j], row[j-1]) + triangle[i][j])
                
                if i == n - 1:
                    result = min(result, temp[j])
            row = temp

        return result