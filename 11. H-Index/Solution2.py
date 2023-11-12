from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index=0
        count=0
        citations.sort(reverse=True)
        for i,citation in enumerate(citations):
            if citation>0:
                if citation>=i+1:
                    h_index=i+1
                else: break
        return h_index


# Example 1:

citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
s=Solution()
print(s.hIndex(citations))

# Example 2:
citations = [1,3,1]
# Output: 1
s=Solution()
print(s.hIndex(citations))

# Example 3:
citations = [0]
# Output: 1
s=Solution()
print(s.hIndex(citations))

# Example 4:
citations = [100]
# Output: 1
s=Solution()
print(s.hIndex(citations))