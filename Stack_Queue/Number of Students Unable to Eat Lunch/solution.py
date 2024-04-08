class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one = sum(students)
        zero = len(students) - one

        for sandwich in sandwiches:
            if sandwich == 0:
                if zero == 0:
                    return one
                zero -= 1
            else:
                if one == 0:
                    return zero
                one -= 1

        return one + zero
