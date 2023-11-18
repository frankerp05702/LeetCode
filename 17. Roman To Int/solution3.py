class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        n = len(s)
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        previous = 0
        for char in s:
            current = roman_to_int[char]
            if current > previous:
                number += current - 2 * previous
            else: 
                number += current
            previous = current
            
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