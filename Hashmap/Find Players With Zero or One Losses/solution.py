class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        lost_store = dict()

        for w, l in matches:
            players.add(w)
            players.add(l)
            if l not in lost_store:
                lost_store[l] = 0
            lost_store[l] += 1

        res = [[], []]
        for p in players:
            if p not in lost_store:
                res[0].append(p)
            elif lost_store[p] == 1:
                res[1].append(p)
        res[0] = sorted(res[0])
        res[1] = sorted(res[1])
        return res
