class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        wordToChar = {}
        charToWord = {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
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