from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wd = {}

        for word in strs:
            s = "".join(sorted(word))
            if s in wd:
                t = wd[s]
                t.append(word)
            else:
                wd[s] = [word]*1

        return list(wd.values())


# Example 1:
strs = ["eat","tea","tan","ate","nat","bat"]
expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
s = Solution()
result = s.groupAnagrams(strs)
print(result)
print(result == expected)

# Example 2:
strs = [""]
expected = [[""]]
s = Solution()
result = s.groupAnagrams(strs)
print(result)
print(result == expected)

# Example 3:
strs = ["a"]
expected = [["a"]]
s = Solution()
result = s.groupAnagrams(strs)
print(result)
print(result == expected)