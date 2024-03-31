class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        res = 0
        while numBottles > 0 or empty >= numExchange:
            if numBottles > 0:
                res += numBottles
                empty += numBottles
                numBottles = 0
            if empty > 0 and empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1

        return res
