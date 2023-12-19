class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        smooth = [[0, 0], [0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, -0], [-1, 1], [-1, -1]]
        for i in range(m):
            for j in range(n):
                count = 0
                total = 0
                for a, b in smooth:
                    x = i + a
                    y = j + b
                    if x >= 0 and x < m and y >= 0 and y < n:
                        count += 1
                        total += img[x][y]
                res[i][j] = total // count
        return res
