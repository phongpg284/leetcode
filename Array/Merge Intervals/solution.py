class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        curr = 0
        next = 1
        intervals = sorted(intervals, key=lambda x: x[0])
        while curr < len(intervals) and next < len(intervals):
            if intervals[curr][1] >= intervals[next][0]:
                intervals[curr][1] = max(intervals[curr][1], intervals[next][1])
            else: 
                result.append(intervals[curr])
                curr = next
            next += 1
        result.append(intervals[curr])
        return result
