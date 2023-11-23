class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        start = 0
        match = False
        for j, c in enumerate(s):
            for i in range(start, len(t)):
                match = False
                if t[i] == c:
                    match = True
                    start = i + 1
                    if j == len(s) - 1:
                        return True
                    break
            if not match: return False
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