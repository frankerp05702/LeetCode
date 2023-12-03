from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_count = Counter(ransomNote)
        mg_count = Counter(magazine)

        for letter in ransomNote:
            if letter not in magazine:
                return False
            else:
                if rn_count[letter] > mg_count[letter]:
                    return False
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
