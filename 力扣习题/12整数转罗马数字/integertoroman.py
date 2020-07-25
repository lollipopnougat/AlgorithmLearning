class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        reps = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        for i in range(13):
            while num >= values[i]:
                num -= values[i]
                res += reps[i]
        return res


class Solution2:
    '''
    闲的蛋疼
    '''
    def intToRoman(self, num: int) -> str:
        if num >= 1000:
            le = (num // 1000)
            return 'M' * le + self.intToRoman(num - 1000 * le)
        elif num >= 900:
            return 'CM' + self.intToRoman(num - 900)
        elif num >= 500:
            return 'D' + self.intToRoman(num - 500)
        elif num >= 400:
            return 'CD' + self.intToRoman(num - 400)
        elif num >= 100:
            return 'C' + self.intToRoman(num - 100)
        elif num >= 90:
            return 'XC' + self.intToRoman(num - 90)
        elif num >= 50:
            return 'L' + self.intToRoman(num - 50)
        elif num >= 40:
            return 'XL' + self.intToRoman(num - 40)
        elif num >= 10:
            return 'X' + self.intToRoman(num - 10)
        elif num >= 9:
            return 'IX' + self.intToRoman(num - 9)
        elif num >= 5:
            return 'V' + self.intToRoman(num - 5)
        elif num == 4:
            return 'IV' + self.intToRoman(num - 4)
        elif num >= 1:
            return 'I' + self.intToRoman(num - 1)
        else:
            return ''

s = Solution()

print(s.intToRoman(10))