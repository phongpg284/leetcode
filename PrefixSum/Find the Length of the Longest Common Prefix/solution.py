class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = dict()
        res = 0

        for num in arr1:
            temp = ""
            for c in str(num):
                temp += c
                prefix[temp] = prefix.get(temp, 0) + 1

        for num in arr2:
            temp = ""
            for c in str(num):
                temp += c
                if temp in prefix:
                    res = max(res, len(temp))

        return res
