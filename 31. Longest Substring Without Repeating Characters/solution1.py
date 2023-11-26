class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, max_length = 0, 0
        reg = {}
        if n < 2: return n
        for right, char in enumerate(s):
            if char in reg: # Repeated
                # Delete all registers from 'left' until the prev occurrence of char
                while s[left] != char:
                    if s[left] in reg:
                        del reg[s[left]]
                    left += 1
                left += 1
            else:
                reg[char] = 1
            max_length = max(max_length, right - left  + 1)
        return max_length



# Example 1:
s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
sol = Solution()
result = sol.lengthOfLongestSubstring(s)
print(result)
print(result == 3)

# Example 2:
s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
sol = Solution()
result = sol.lengthOfLongestSubstring(s)
print(result)
print(result == 1)

# Example 3:
s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
sol = Solution()
result = sol.lengthOfLongestSubstring(s)
print(result)
print(result == 3)

# Example 4:
s = " "
# Output: 1
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
sol = Solution()
result = sol.lengthOfLongestSubstring(s)
print(result)
print(result == 1)