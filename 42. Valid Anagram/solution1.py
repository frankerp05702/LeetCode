from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Example 1:
s = "anagram"
t = "nagaram"
# Output: true
sol = Solution()
result = sol.isAnagram(s, t)
print(result)
print(result == True)


# Example 2:
s = "rat"
t = "car"
# Output: false
sol = Solution()
result = sol.isAnagram(s, t)
print(result)
print(result == False)