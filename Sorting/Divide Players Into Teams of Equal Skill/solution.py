class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        n = len(skill)
        res = 0
        total = skill[0] + skill[-1]

        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != total:
                return -1
            res += skill[i] * skill[n - 1 - i]
        return res
    