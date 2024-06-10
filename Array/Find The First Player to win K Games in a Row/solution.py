class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        max_val = max(skills)
        max_index = skills.index(max_val)

        i = 0
        cur_max = skills[0]
        cur = 0
        cur_index = 0
        while i < max_index:
            i += 1
            if skills[i] < cur_max:
                cur += 1
            else:
                cur_index = i
                cur = 1
                cur_max = skills[i]
            if cur == k:
                return cur_index

        return max_index
