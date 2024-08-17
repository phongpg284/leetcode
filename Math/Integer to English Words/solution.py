class Solution:
    def numberToWords(self, num: int) -> str:
        nums = [
            1000000000,
            1000000,
            1000,
            100,
            90,
            80,
            70,
            60,
            50,
            40,
            30,
            20,
            19,
            18,
            17,
            16,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
        ]

        words = [
            "Billion",
            "Million",
            "Thousand",
            "Hundred",
            "Ninety",
            "Eighty",
            "Seventy",
            "Sixty",
            "Fifty",
            "Forty",
            "Thirty",
            "Twenty",
            "Nineteen",
            "Eighteen",
            "Seventeen",
            "Sixteen",
            "Fifteen",
            "Fourteen",
            "Thirteen",
            "Twelve",
            "Eleven",
            "Ten",
            "Nine",
            "Eight",
            "Seven",
            "Six",
            "Five",
            "Four",
            "Three",
            "Two",
            "One",
        ]

        res = ""

        for i in range(len(nums)):
            if num >= nums[i]:
                if num >= 100:
                    res += self.numberToWords(num /
                                              nums[i]) + " " + words[i] + " "
                else:
                    res += words[i] + " "

                num %= nums[i]

                if num == 0:
                    break

        return res[:-1] if res else "Zero"
