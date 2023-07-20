class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        res = []

        for i in range(n):
            if not res or asteroids[i] > 0:
                res.append(asteroids[i])
            else:
                while res and res[-1] > 0 and res[-1] < abs(asteroids[i]):
                    res.pop()
                if res and res[-1] == abs(asteroids[i]):
                    res.pop()
                else:
                    if not res or res[-1] < 0:
                        res.append(asteroids[i])
        return res