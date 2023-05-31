class UndergroundSystem:

    def __init__(self):
        self.trips = dict()        
        self.customers = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (startStation, start) = self.customers[id]
        station = (startStation, stationName)

        if station in self.trips:
            (time, total) = self.trips[station]
            self.trips[station] = (time + t - start, total + 1)
        else:
            self.trips[(startStation, stationName)] = (t - start, 1)
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        station = (startStation, endStation)
        (time, total) = self.trips[station]

        return time/total


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)