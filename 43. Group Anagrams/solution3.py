from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wd = collections.defaultdict(list)

        for word in strs:
            wd["".join(sorted(word))].append(word)

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