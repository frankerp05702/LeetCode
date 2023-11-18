class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        roman_to_int = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        previous = ""
        for letter in s:
            # If previous for the first time, save it and continue
            if not previous:
                if letter == "I" or letter == "X" or letter == "C":
                    previous = letter
                    continue
            # Try converting (letter + previous)
            try:
                num = roman_to_int[previous + letter]
                number += num
                previous = ""
            except KeyError:
                number += roman_to_int[previous]
                previous = ""
                # If letter is previous
                if letter == "I" or letter == "X" or letter == "C":
                        previous = letter
                        continue
                else:
                    number += roman_to_int[letter]
        
        if previous: number += roman_to_int[previous]

        return number

# Example 1:

s = "III"
# Output: 3
# Explanation: III = 3.
sol = Solution()
result = sol.romanToInt(s)
print(result)
print(result==3)

# Example 2:

s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
sol = Solution()
result = sol.romanToInt(s)
print(result)
print(result==58)

# Example 3:

s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
sol = Solution()
result = sol.romanToInt(s)
print(result)
print(result==1994)