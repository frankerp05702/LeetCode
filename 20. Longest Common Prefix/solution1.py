from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n = len(strs)

        common = True
        j = 0
        compare = ""
        while common:
            prefix += compare
            letter = ""
            for i in range(n):
                word = strs[i]
                try:
                    letter = word[j]
                except IndexError:
                    common = False
                if i == 0:
                    compare = letter
                else:
                    if letter != compare: 
                        common = False
            j += 1    
        return prefix


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