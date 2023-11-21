class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0: return ""
        if numRows == 1: return s

        rows = [""]*numRows
        j = 0
        up_down = True

        for i,char in enumerate(s):
            if j == numRows: break
            rows[j] += char
            if i > 0 and (j == 0 or j == numRows - 1):
                up_down = not up_down
            if up_down: j += 1
            else: j -= 1
        
        return "".join(rows)

# Example 1:

s = "PAYPALISHIRING"
numRows = 3
# Output: "PAHNAPLSIIGYIR"
sol = Solution()
result = sol.convert(s, numRows)
print(result)
print(result=="PAHNAPLSIIGYIR")

# Example 2:

s = "PAYPALISHIRING"
numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
sol = Solution()
result = sol.convert(s, numRows)
print(result)
print(result=="PINALSIGYAHRPI")


# Example 3:

s = "A"
numRows = 1
# Output: "A"
sol = Solution()
result = sol.convert(s, numRows)
print(result)
print(result=="A")

# Example 4
s = "AB"
numRows = 1
sol = Solution()
result = sol.convert(s, numRows)
print(result)
print(result=="AB")

# Example 5
s = "ABC"
numRows = 2
sol = Solution()
result = sol.convert(s, numRows)
print(result)
print(result=="ACB")