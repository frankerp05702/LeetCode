from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem=None
        freq={}
        for num in nums:
            freq[num]=0
        for num in nums:
            freq[num]+=1

        for key in freq.keys():
            if freq[key]>len(nums)/2:
                elem=key
                break
        
        return elem

# Example 1:
nums = [3,2,3]
# Output: 3
s = Solution()
elem = s.majorityElement(nums)
print(elem)

# Example 2:
nums = [2,2,1,1,1,2,2]
# Output: 2
s = Solution()
elem = s.majorityElement(nums)
print(elem)

