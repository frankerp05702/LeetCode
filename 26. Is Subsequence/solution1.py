class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        i = 0
        for j, c in enumerate(s):
            if i < len(t):
                try:
                    index = t.index(c, i)
                    i = index + 1
                    if j < len(s) - 1: continue
                    else: return True
                except ValueError:
                    return False
        
        return False


# Example 1:

s = "abc"
t = "ahbgdc"
expected = True
sol = Solution()
result = sol.isSubsequence(s, t)
print(result)
if result == expected: print("OK")
else: print("X")

# Example 2:

s = "axc"
t = "ahbgdc"
# Output: false
expected = False
sol = Solution()
result = sol.isSubsequence(s, t)
print(result)
if result == expected: print("OK")
else: print("X")