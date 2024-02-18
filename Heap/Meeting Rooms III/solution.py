class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        count = [0] * n
        free_rooms = list(range(n))
        busy_rooms = []

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
            else:
                end_time, room = heapq.heappop(busy_rooms)
                end += end_time - start

            heapq.heappush(busy_rooms, (end, room))
            count[room] += 1

        return count.index(max(count))
