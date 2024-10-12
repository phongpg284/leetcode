class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        left, right = 0, len(self.calendar)
        while left < right:
            mid = (left + right) // 2
            if self.calendar[mid][1] <= start:
                left = mid + 1
            else:
                right = mid

        if left == len(self.calendar):
            self.calendar.append((start, end))
            return True

        if self.calendar[left][0] >= end:
            self.calendar.insert(left, (start, end))
            return True

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
