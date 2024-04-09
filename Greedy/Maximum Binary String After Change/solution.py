class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        sum = binary.count('0')
        zero_mark = binary.find('0')

        if sum == 0:
            return binary

        res = ['1'] * len(binary)
        res[sum + zero_mark - 1] = '0'
        return ''.join(res)
