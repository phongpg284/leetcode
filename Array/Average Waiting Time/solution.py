class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        current_time = 0
        for arrival, time in customers:
            if current_time > arrival:
                res += time + current_time - arrival
                current_time += time
            else:
                res += time
                current_time = arrival + time
        return res / len(customers)
