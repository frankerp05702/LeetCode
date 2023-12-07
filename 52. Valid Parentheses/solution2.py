class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        parenths = {")": "(", "]": "[", "}": "{"}
        if n % 2 != 0: return False

        stack = ['a']*(n + 1)
        top = -1
        for c in s:
            if c not in parenths:
                top += 1
                stack[top] = c
            else:
                if top < 0: return False
                else:
                    if stack[top] != parenths[c]:
                        return False
                    top -= 1

        if top > 0: return False
        return True

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