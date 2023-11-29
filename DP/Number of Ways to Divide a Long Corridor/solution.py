class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        n = len(corridor)
        res = 1
        seats = []
        
        for i in range(n):
            if corridor[i] == 'S': 
                seats.append(i)
                if len(seats) == 3:
                    res *= (seats[2] - seats[1])
                    seats = [i]
        
        if len(seats) <= 1:
            return 0
        
        return res % mod