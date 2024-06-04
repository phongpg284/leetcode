class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        res = ''
        t = ''
        pos = defaultdict(list)
        for i in range(n):
            pos[s[i]].append(i)

        i = 0
        while i < n:
            if not t:
                t += s[i]
                i += 1
            else:
                for j in range(ord('a'), ord(t[-1])):
                    c = chr(j)

                    next_idx = bisect_left(pos[c], i)
                    if next_idx < len(pos[c]):
                        while i <= pos[c][next_idx]:
                            t += s[i]
                            i += 1
                        break
                res += t[-1]
                t = t[:-1]

        res += t[::-1]
        return res
