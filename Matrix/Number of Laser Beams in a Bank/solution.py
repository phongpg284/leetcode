class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        t = 0

        for row in bank:
            lasers = row.count('1')
            if lasers == 0:
                continue
            res += lasers * t
            t = lasers
        return res
