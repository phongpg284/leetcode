class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        return self.combination_recur(candidates, target, [])

    def combination_recur(self, candidates, target, result):
        if target == 0:
            return [result]
        res = []
        for i in range(len(candidates)):
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue
            if candidates[i] > target:
                break
            else:
                new_result = result[::]
                new_result.append(candidates[i])
                new_candidates = candidates[i + 1:] 
                combination = self.combination_recur(new_candidates, target - candidates[i], new_result)
                res = res + combination
        return res