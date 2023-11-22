class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        i = 0
        j = len(low) - 1
        while i < j:
            while not low[i].isalnum():
                i += 1
            while not low[j].isalnum():
                j -= 1
            if low[i] != low[j]:
                break
            i += 1
            j -= 1

# Example 1:
s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
sol = Solution()
result = sol.isPalindrome(s)
print(result)

# Example 2:
s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
sol = Solution()
result = sol.isPalindrome(s)
print(result)

# Example 3:
s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
sol = Solution()
result = sol.isPalindrome(s)
print(result)