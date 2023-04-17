class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for word in strs:
            key = "".join(sorted(word))
            if key in hashmap:
                hashmap[key] = hashmap[key] + [word]
            else:
                hashmap[key] = [word]
        return list(hashmap.values())