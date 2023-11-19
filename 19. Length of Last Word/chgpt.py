class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing spaces
        if not s:
            return 0
        
        last_word_length = 0
        for char in s[::-1]:  # Iterate in reverse
            if char != ' ':  # Count the characters until a space is encountered
                last_word_length += 1
            else:
                break  # Break when space is encountered (end of the last word)
        
        return last_word_length

# Example 1:
s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
sol = Solution()
result = sol.lengthOfLastWord(s)
print(result)
print(result==5)
    

# Example 2:
s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
sol = Solution()
result = sol.lengthOfLastWord(s)
print(result) 
print(result==4) 


# Example 3:
s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
sol = Solution()
result = sol.lengthOfLastWord(s)
print(result)
print(result==6)