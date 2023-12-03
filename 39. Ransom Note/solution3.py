class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))

# Example 1:
ransomNote = "a"
magazine = "b"
# Output: false
s = Solution()
result = s.canConstruct(ransomNote, magazine)
print(result)
print(result == False)

# Example 2:
ransomNote = "aa"
magazine = "ab"
# Output: false
s = Solution()
result = s.canConstruct(ransomNote, magazine)
print(result)
print(result == False)

# Example 3:
ransomNote = "aa"
magazine = "aab"
# Output: true
s = Solution()
result = s.canConstruct(ransomNote, magazine)
print(result)
print(result == True)
