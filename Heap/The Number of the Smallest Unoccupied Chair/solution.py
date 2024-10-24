class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        sort_times = sorted([(times[i], i) for i in range(n)])
        sort_index = [time[1] for time in sort_times]
        empty, take = list(range(len(times))), []

        for i in sort_index:
            arrive_time, leave_time = times[i]

            while take and take[0][0] <= arrive_time:
                heappush(empty, heappop(take)[1])

            seat = heappop(empty)

            if i == targetFriend:
                return seat

            heappush(take, (leave_time, seat))
