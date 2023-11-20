from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        
        # Sort words to compare first and last words
        strs.sort()
        first = strs[0]
        last = strs[-1]

        # Compare characters in first and last until we are out of characters or until not match.
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]


# Example 1:
strs = ["flower","flow","flight"]
# Output: "fl"
sol = Solution()
result = sol.longestCommonPrefix(strs)
print(result)
print(result=="fl")

# Example 2:
strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
sol = Solution()
result = sol.longestCommonPrefix(strs)
print(result)
print(result=="")