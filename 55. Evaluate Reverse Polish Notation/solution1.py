from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_operators = {"+", "-", "*", "/"}
        
        for c in tokens:
            if c not in valid_operators:
                stack.append(int(c))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                match c:
                    case "+":
                        stack.append(op1 + op2)
                    case "-":
                        stack.append(op1 - op2)
                    case "*":
                        stack.append(op1 * op2)
                    case "/":
                        stack.append(int(op1 / op2))

        return stack[0]


# Example 1:
tokens = ["2","1","+","3","*"]
expected = 9
# Explanation: ((2 + 1) * 3) = 9
s = Solution()
result = s.evalRPN(tokens)
print(result)
print(result == expected)

# Example 2:
tokens = ["4","13","5","/","+"]
expected = 6
# Explanation: (4 + (13 / 5)) = 6
s = Solution()
result = s.evalRPN(tokens)
print(result)
print(result == expected)

# Example 3:
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
expected = 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
s = Solution()
result = s.evalRPN(tokens)
print(result)
print(result == expected)