class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        count = [0] * n
        free_rooms = list(range(n))
        busy_rooms = []

        for start, end in meetings:
            # free up busy room 
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            # assign to lowest index free room
            if free_rooms:
                room = heapq.heappop(free_rooms)
            # Delay until the earliest room gets free
            else:
                end_time, room = heapq.heappop(busy_rooms)
                end += end_time - start

            # Book new room
            heapq.heappush(busy_rooms, (end, room))
            count[room] += 1

        return count.index(max(count))
