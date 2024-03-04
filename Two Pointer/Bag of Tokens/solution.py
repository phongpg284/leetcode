class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens = sorted(tokens)
        i = 0
        j = n - 1
        t = 0
        res = 0
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                t += 1
                i += 1
            else:
                if res == 0:
                    break
                power += tokens[j]
                j -= 1
                t -= 1
            res = max(res, t)
        return res
