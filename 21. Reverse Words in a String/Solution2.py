class Solution:
    def join_word_to_reverted(self, reverted: str, word: str) -> str:
        if word: 
            if reverted: 
                reverted = word + " " + reverted
            else:
                reverted = word
        return reverted
    def reverseWords(self, s: str) -> str:
        reverted = ""
        word = ""
        should_join = False
        for letter in s:
            if letter == " ":
                should_join = True
            else: 
                if should_join:
                    reverted = self.join_word_to_reverted(reverted, word)
                    word = ""
                word += letter
                should_join = False
        reverted = self.join_word_to_reverted(reverted, word)
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