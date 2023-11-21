class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try: 
            result = haystack.index(needle)
        except ValueError:
            result = -1
        return result

# Example 1:

haystack = "sadbutsad"
needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
sol = Solution()
result = sol.strStr(haystack, needle)
print(result)
print(result == 0)

# Example 2:

haystack = "leetcode"
needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
sol = Solution()
result = sol.strStr(haystack, needle)
print(result)
print(result == -1)