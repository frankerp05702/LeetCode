from collections import Counter


class Solution:
    def sContainsT(self, t: str, w_counter: Counter, t_counter: Counter) -> bool:
        isContained = True
        for char in t:
            if t_counter[char] > w_counter[char]:
                isContained = False
                break
        return isContained
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        t_counter = Counter(t)

        if n == 0 or m == 0: return ""

        window = s*5
        start = 0
        end = start + m
        while end <= n:
            window_ok = True
            while start <= n - m and start <= end and window_ok:
                # Given the window from start to end
                w = s[start:end]
                w_counter = Counter(w)
                # If all the letters are contained in the window
                if self.sContainsT(t, w_counter, t_counter):
                    window = w if len(w) < len(window) else window
                    start += 1
                else:
                    window_ok = False
            end += 1       

        return window if len(window) <= n else ""

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