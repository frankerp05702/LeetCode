class Solution:
    def sContainsT(self, t: str, w_counter, t_counter) -> bool:
        isContained = True
        for char in t:
            if char not in w_counter or t_counter[char] > w_counter[char]:
                isContained = False
                break
        return isContained
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        t_counter, w_counter = {}, {}

        if n == 0 or m == 0: return ""

        window = s*5
        start, end = 0, m

        # Count t for the only one time
        for char in t:
            if char in t_counter: t_counter[char] += 1
            else: t_counter[char] = 1

        # Count window for the first time
        w = s[start:end]
        for char in w:
            if char in w_counter: w_counter[char] += 1
            else: w_counter[char] = 1

        while end <= n:
            window_ok = True
            while start <= n - m and start <= end and window_ok:
                w = s[start:end]
                # If all the letters are contained in the window
                if self.sContainsT(t, w_counter, t_counter):
                    window = w if len(w) < len(window) else window
                    if w_counter[s[start]] > 1: w_counter[s[start]] -= 1 
                    else: del w_counter[s[start]]
                    start += 1
                else:
                    window_ok = False
             
            if end < n:
                if s[end] in w_counter: w_counter[s[end]] += 1
                else: w_counter[s[end]] = 1
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