from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index=0
        h_dict={}
        for h in range(10):
                h_dict[h]=0
        for citation in citations:
            for h in range(citation):
                h_dict[h+1]+=1
        for h in h_dict.keys():
             if h_dict[h]>=h: 
                  h_index=h
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