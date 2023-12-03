class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if not s or not pattern: return False
        sp = s.split()
        if len(sp) != len(pattern): return False

        wp = {}

        for i, char in enumerate(pattern):
            if char not in wp:
                if sp[i] in wp.values():
                    return False
                else:
                    wp[char] = sp[i]
            else:
                if wp[char] != sp[i]: return False

        return True

# Example 1:
pattern = "abba"
s = "dog cat cat dog"
# Output: true
sol = Solution()
result = sol.wordPattern(pattern, s)
print(result)
print(result == True)


# Example 2:
pattern = "abba"
s = "dog cat cat fish"
# Output: false
sol = Solution()
result = sol.wordPattern(pattern, s)
print(result)
print(result == False)


# Example 3:
pattern = "aaaa"
s = "dog cat cat dog"
# Output: false
sol = Solution()
result = sol.wordPattern(pattern, s)
print(result)
print(result == False)