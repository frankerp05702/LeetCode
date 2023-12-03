class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped = set(zip(s, t))
        if len(zipped)==len(set(s))== len(set(t)):
            return True
        else:
            return False

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