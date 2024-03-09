class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        t = [[student_score[k], student_score] for student_score in score]

        t = sorted(t)

        return [score for _, score in t[::-1]]