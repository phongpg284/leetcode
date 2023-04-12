class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == '':
            return []
        return self.recur_digits(result, "", 0, digits)

    def recur_digits(self, result, current_str, digit_index, digits):
        if (digit_index == len(digits)):
            result.append(current_str)
            return result       

        digit = digits[digit_index]
        chars = self.get_chars(digit)

        for char in chars:
            self.recur_digits(result, current_str + char,  digit_index + 1, digits)

        return result

    def get_chars(self, num):
        num = int(num)
        if (num == 7):
            return [chr(num * 3 + 91), chr(num * 3 + 92), chr(num * 3 + 93), chr(num * 3 + 94)]
        if (num == 8):
            return [chr(num * 3 + 92), chr(num * 3 + 93), chr(num * 3 + 94)]
        elif (num == 9):
            return [chr(num * 3 + 92), chr(num * 3 + 93), chr(num * 3 + 94), chr(num * 3 + 95)]
        else:
            return [chr(num * 3 + 91), chr(num * 3 + 92), chr(num * 3 + 93)]