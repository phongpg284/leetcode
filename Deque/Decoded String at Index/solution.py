class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0

        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1

        for j in range(i - 1, -1, -1):
            if s[j].isdigit():
                length //= int(s[j])
                k %= length
            else:
                if k == 0 or k == length:
                    return s[j]
                length -= 1