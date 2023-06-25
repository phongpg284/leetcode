class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        return self.travel(locations, finish, start, fuel, dp)
    '''
        dp[i][j] represents number of ways traver to from current to finish with remaining fuel
    '''
    def travel(self, locations, finish, current, fuel, dp):
        mod = 10** 9 + 7
        if fuel < 0: 
            return 0
        
        if dp[current][fuel] > -1:
            return dp[current][fuel]

        res = 1 if current == finish else 0
        
        for city in range(len(locations)):
            if city != current and fuel >= abs(locations[current] - locations[city]):
                new_fuel = fuel - abs(locations[current] - locations[city])
                res += self.travel(locations, finish, city, new_fuel, dp) % mod
        
        res = res % mod 
        dp[current][fuel] = res
        return res
