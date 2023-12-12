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
    def calculate(self, s: str) -> int:
        s = "".join([c for c in s if c != " "])
        n = len(s)
        operators = {
            "+": {
                "precedence": 2,
                "asociativity": "left"
            }, 
            "-": {
                "precedence": 2,
                "asociativity": "left"
            }, 
            "*": {
                "precedence": 3,
                "asociativity": "left"
            },
            "/": {
                "precedence": 3,
                "asociativity": "left"
            }
            }

        rpn_output = []
        op_stack = []
        # Convert to Reverse Polish Notation
        for i, token in enumerate(s):
        # If there is a token, read the token
        # Tokens can be
            # A number...Add it to output
            if token.isnumeric():
                if i > 0 and s[i - 1].isnumeric():
                    token = rpn_output.pop() + token
                rpn_output.append(token)
            # A function...Add it to the op_stack
            # An operator O1
            elif token in operators:
                # Convert unary "-" to binary "-" by adding a "0" as first operand
                if token == "-":
                    if i == 0 or s[i - 1] == "(": 
                        rpn_output.append("0")
                # Normal application of shuntyard algorithm
                operator_o1 = token
                if not op_stack: op_stack.append(operator_o1)
                else:
                    operator_o2 = op_stack[-1]
                    if op_stack[-1] != "(":
                        if operators[operator_o1]["precedence"] < operators[operator_o2]["precedence"] or (
                            operators[operator_o1]["precedence"] == operators[operator_o2]["precedence"] and 
                            operators[operator_o1]["asociativity"] == "left"):
                            rpn_output.append(op_stack.pop())
                    op_stack.append(operator_o1)
            # A ","
            # A left parenthesis "("
            elif token == "(":
                op_stack.append(token)
            # A right parenthesis ")" 
            elif token == ")":
                found_open_parenthesis = False
                while op_stack:
                    if op_stack[-1] == "(":
                        found_open_parenthesis = True
                        break
                    else:
                        rpn_output.append(op_stack.pop())
                if not found_open_parenthesis:
                    return None # There is a mismatch parenthesis, invalid expression
                else:
                    op_stack.pop()
        while op_stack:
            if op_stack[-1] != "(": rpn_output.append(op_stack.pop())                
                
        return self.evalRPN(rpn_output)
                
                


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
