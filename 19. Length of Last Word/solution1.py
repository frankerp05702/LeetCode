class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = s.split()
        return len(splitted[len(splitted)-1])

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
