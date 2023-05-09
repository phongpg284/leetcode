class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        '''
        Find start index where to insert start new intervals
        '''
        left = 0
        right = len(intervals) - 1
        start = -1
        while left <= right:
            middle = (left + right) // 2
            if (intervals[middle][0] <= newInterval[0] and (middle == len(intervals) - 1 or intervals[middle + 1][0] >= newInterval[0])):
                start = middle
                break
            elif intervals[middle][0] >= newInterval[0]:
                right = middle - 1
            else:
                left = middle + 1
        '''
        Find end index where to insert end of new intervals
        '''
        left = 0
        right = len(intervals) - 1
        end = len(intervals)
        
        while left <= right:
            middle = (left + right) // 2
            if intervals[middle][1] >= newInterval[1] and (middle == 0 or intervals[middle - 1][1] <= newInterval[1]):
                end = middle
                break
            elif intervals[middle][1] >= newInterval[1]:
                right = middle - 1
            else:
                left = middle + 1
        
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