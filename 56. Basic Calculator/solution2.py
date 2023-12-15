from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        digit_stack, sign_stack = [], []
        res = num = 0
        sign = 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                sign = 1
                num = 0
            elif c == "-":
                res += sign * num
                sign = -1
                num = 0
            elif c == "(":
                digit_stack.append(res)
                sign_stack.append(sign)
                num = 0
                sign = 1
                res = 0
            elif c == ")":
                res += sign * num
                res = res * sign_stack.pop() + digit_stack.pop()
                num = 0
        
        if num != 0:
            res += sign * num

        return res             
                


# Example 1:
s = "1 + 1"
expected = 2
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)

# Example 2:
s = " 2-1 + 2 "
expected = 3
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)


# Example 3:
s = "(1+(4+5+2)-3)+(6+8)"
expected = 23
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)

# Example 4:
s = "1-(     -2)"
expected = 3
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)

# Example 5:
s = "-2+ 1"
expected = -1
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)


# Example 6:
s = "1-11"
expected = -10
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)

# Example 7:
s = "2-4-(8+2-6+(8+4-(1)+8-10))"
expected = -15
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)

# Example 8:
s = "- (3 - (- (4 + 5) ) )"
expected = -12
sol = Solution()
result = sol.calculate(s)
print(result)
print(result == expected)
