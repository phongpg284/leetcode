class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    valid = True
                    for k in range(n):
                        if mat[i][k] == 1 and k != j:
                            valid = False
                            break
                    for k in range(m):
                        if mat[k][j] == 1 and k != i:
                            valid = False
                            break
                    if valid:
                        res += 1
        return res 