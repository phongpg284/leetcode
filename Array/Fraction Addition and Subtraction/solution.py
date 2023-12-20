class Solution:
    def fractionAddition(self, expression: str) -> str:
        dif = 10 ** (-8)
        expression = expression.replace('-', "+-")
        fractions = expression.split('+')

        res = 0
        for fraction in fractions:
            if fraction != "":
                [up, down] = fraction.split('/')
                res += int(up) / int(down)

        if round(res) == res:
            return str(round(res)) + '/1'

        i = 1
        while True:
            rev = i / res
            if (abs(round(rev) - rev) < dif):
                key = -1 if res < 0 else 1
                return f"{key * i}/{key * round(rev)}"
            i += 1
