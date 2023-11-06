class SeatManager:

    def __init__(self, n: int):
        self.seats = []
        self.last = 0

    def reserve(self) -> int:
        if not self.seats:
            self.last += 1
            return self.last
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)