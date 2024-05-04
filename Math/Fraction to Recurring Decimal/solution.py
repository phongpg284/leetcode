class Solution:
    def fractionToDecimal(self, up: int, down: int) -> str:
        is_negative = (up // down) < 0
        up, down = abs(up), abs(down)
        res = str(up // down)
        cache = dict()

        decimal = None
        up = (up % down) * 10
        temp = ''

        i = 0
        while up:
            if up in cache:
                index = cache[up]
                decimal = temp[:index] + '(' + temp[index:] + ')'
                break

            temp += str(up // down)
            cache[up] = i
            up = (up % down) * 10
            i += 1

        if not decimal:
            decimal = temp

        if decimal:
            res += '.' + decimal
        return '-' + res if is_negative else res
