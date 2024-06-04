class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for h, x in people:
            res.insert(x, (h, x))
        return res
