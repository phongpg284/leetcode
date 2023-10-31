class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        for i in range(len(pref)):
            temp = pref[i] ^ pref[i - 1] if i > 0 else pref[i]
            res.append(temp)
        return res