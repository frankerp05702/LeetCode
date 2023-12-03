class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if len(s) < 1: return False

        ism = {}

        for i, char in enumerate(s):
            if char not in ism:
                if t[i] in ism.values():
                    return False
                else:
                    ism[char] = t[i]
            else:
                if ism[char] != t[i]: return False

        return True

# Example 1:
s = "egg"
t = "add"
# Output: true
sol = Solution()
result = sol.isIsomorphic(s, t)
print(result)
print(result == True)

# Example 2:
s = "foo"
t = "bar"
# Output: false
sol = Solution()
result = sol.isIsomorphic(s, t)
print(result)
print(result == False)

# Example 3:
s = "paper"
t = "title"
# Output: true
sol = Solution()
result = sol.isIsomorphic(s, t)
print(result)
print(result == True)

# Example 4:
s = "badc"
t = "baba"
# Output: true
sol = Solution()
result = sol.isIsomorphic(s, t)
print(result)
print(result == False)

# Example 5:
s = "baba"
t = "baba"
# Output: true
sol = Solution()
result = sol.isIsomorphic(s, t)
print(result)
print(result == True)