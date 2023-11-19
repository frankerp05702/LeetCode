from math import trunc


class Solution:
    def __init__(self):
        self.int_to_roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
    def roman_figures(self, fig: int, base: int) -> str:
        roman = ""

        if fig == 9: roman += self.int_to_roman[9*base]
        elif fig >= 5: 
            roman += self.int_to_roman[5*base]
            roman += self.int_to_roman[1*base]*(fig-5)
        elif fig == 4:
            roman += self.int_to_roman[4*base]
        else:
            roman += self.int_to_roman[1*base]*fig

        return roman

    def intToRoman(self, num: int) -> str:
        roman = ""

        mil = trunc(num/1000)
        roman += self.int_to_roman[1000]*mil

        num -= mil*1000
        cent = trunc(num/100)
        base = 100
        roman += self.roman_figures(cent, base)

        num -= cent*100
        dec = trunc(num/10)
        base = 10
        roman += self.roman_figures(dec, base)

        unit = num - dec*10
        base = 1
        roman += self.roman_figures(unit, base)

        return roman

# Example 1:

num = 3
sol = Solution()
result = sol.intToRoman(num)
print(result)
print(result=="III")

# Example 2:

num = 58
sol = Solution()
result = sol.intToRoman(num)
print(result)
print(result=="LVIII")

# Example 3:

num = 1994
sol = Solution()
result = sol.intToRoman(num)
print(result)
print(result=="MCMXCIV")