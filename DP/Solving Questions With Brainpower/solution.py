class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * length
        for i in range(length -1, -1, -1):
            [point, brainpower] = questions[i]

            # Index of next question can take if take questions[i]
            valid = i + brainpower + 1

            if i == length - 1:
                dp[i] = point
            elif valid < length:
                dp[i] = max(dp[i+1], point + dp[valid])
            else:
                dp[i] = max(dp[i+1], point)

        return dp[0]