class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        hashmap = set()
        return self.combination_recur(candidates, target, [], hashmap)

    def combination_recur(self, candidates, target, result, hashmap):
        if target == 0:
            sort_result = tuple(sorted(result))
            if sort_result in hashmap:
                return []
            else:
                hashmap.add(sort_result)
                return [result]
        res = []
        for i in range(len(candidates)):
            if candidates[i] <= target:
                new_result = result[::]
                new_result.append(candidates[i])
                new_candidates = candidates[i:] 
                combination = self.combination_recur(new_candidates, target - candidates[i], new_result, hashmap)
                res = res + combination
        return res
