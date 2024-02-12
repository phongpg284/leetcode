class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        actions = defaultdict(set)
        for id, min in logs:
            actions[id].add(min)

        res = [0] * k
        for val in actions.values():
            res[len(val) - 1] += 1
        
        return res
