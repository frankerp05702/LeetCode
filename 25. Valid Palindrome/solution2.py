from math import trunc


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c.lower() for c in s if c.lower().isalnum()]
        n = len(clean)
        if n < 2:  return True
        if n == 2: return clean[0]==clean[1]
        if n == 3: return clean[0]==clean[2]

        i = 0; j = n - 1
        k = trunc(n / 2) - 1
        l = trunc(n / 2)
        if not n % 2 == 0: l += 1

        while i < k and j > l:
            if clean[i] != clean[j] or  clean[k] != clean[l]: return False
            i += 1; j -= 1
            k -= 1; l += 1

        return True

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