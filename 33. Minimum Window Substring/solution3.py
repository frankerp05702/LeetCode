from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        t_count = Counter(t)
        w_count = {}
        min_length = float('inf')
        min_window = ""

        if not s or not t: return ""

        start = 0
        matches = 0
        for end in range(n):
            char = s[end]
            w_count[char] = w_count.get(char, 0) + 1

            if w_count[char] == t_count[char]:
                matches += 1

            while matches == len(t_count) and start <= end:
                char = s[start]

                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    min_window = s[start:end + 1]

                w_count[char] -= 1
                if char in t_count and w_count[char] < t_count[char]:
                    matches -= 1                
                
                start += 1

        return min_window

        

# Example 1:
s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "BANC")

# Example 2:
s = "a"
t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "a")

# Example 3:
s = "a"
t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "")

# Example 4:
s = "a"
t = "a"
# Output: "a"
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "a")

# Example 5:
s = "abc"
t = "cba"
# Output: "abc"
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "abc")

# Example 5:
s = "ab"
t = "a"
# Output: "a"
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "a")

# Example 6:
s = "cabwefgewcwaefgcf"
t = "cae"
# Output: "cwae"
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "cwae")

# Example 7:
s = "aa"
t = "aa"
# Output: "aa"
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
sol = Solution()
result = sol.minWindow(s, t)
print(result)
print(result == "aa")