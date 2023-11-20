class Solution:
    def reverseWords(self, s: str) -> str:
        reverted = ""
        splitted = s.split(None)

        reverted = " ".join(splitted[::-1])

        return reverted

# Example 1:

s = "the sky is blue"
# Output: "blue is sky the"
sol = Solution()
result = sol.reverseWords(s)
print(result)
print(result=="blue is sky the")

# Example 2:

s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
sol = Solution()
result = sol.reverseWords(s)
print(result)
print(result=="world hello")

# Example 3:

s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
sol = Solution()
result = sol.reverseWords(s)
print(result)
print(result=="example good a")