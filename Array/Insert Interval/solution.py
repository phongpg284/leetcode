class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        left, right = 0, n - 1
        start = -1
        '''
        Find start index where to insert start new intervals
        '''
        while left <= right:
            mid = (left + right) // 2
            if (intervals[mid][0] <= newInterval[0] and (mid == len(intervals) - 1 or intervals[mid + 1][0] >= newInterval[0])):
                start = mid
                break
            elif intervals[mid][0] >= newInterval[0]:
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, n - 1
        end = n
        '''
        Find end index where to insert end of new intervals
        '''
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][1] >= newInterval[1] and (mid == 0 or intervals[mid - 1][1] <= newInterval[1]):
                end = mid
                break
            elif intervals[mid][1] >= newInterval[1]:
                right = mid - 1
            else:
                left = mid + 1

        '''
        Modify new intervals to remove overlapping
        '''
        if start > -1 and newInterval[0] <= intervals[start][1]:
            newInterval[0] = intervals[start][0]
            start -= 1
        if end < len(intervals) and newInterval[1] >= intervals[end][0]:
            newInterval[1] = intervals[end][1]
            end += 1

        intervals = intervals[:start + 1] + [newInterval] + intervals[end:]
        return intervals
