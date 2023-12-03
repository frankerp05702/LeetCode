class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        checked = set()
        for letter in ransomNote:
            if letter in checked: continue
            if letter not in magazine:
                return False
            else:
                if ransomNote.count(letter) > magazine.count(letter):
                    return False
            checked.add(letter)
        return True

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
