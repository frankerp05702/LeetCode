class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        parenths = {")": "(", "]": "[", "}": "{"}
        if n % 2 != 0: return False

        opens = []
        for c in s:
            if c not in parenths:
                opens.append(c)
            else:
                if not opens: return False
                else: 
                    if opens.pop(-1) != parenths[c]:
                        return False

        return not opens

# Example 1:
s = "()"
# Output: true
sol = Solution()
result = sol.isValid(s)
print(result)
print(result == True)


# Example 2:
s = "()[]{}"
# Output: true
sol = Solution()
result = sol.isValid(s)
print(result)
print(result == True)


# Example 3:
s = "(]"
# Output: false
sol = Solution()
result = sol.isValid(s)
print(result)
print(result == False)