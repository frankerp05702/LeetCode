from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq={}
        # As numbers are ordered
        for num in nums:    
            freq[num]=0

        for num in nums:
            if freq[num]<2: 
                freq[num]+=1

        keys = list(freq.keys())
        pos=0
        for key in keys:
            for i in range(freq[key]):
                nums[pos]=key
                pos+=1

        return pos


# Example 1:
nums = [1,1,1,2,2,3]
# Output: 2, nums = [1,2,_]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)

# Example 2:
nums = [0,0,1,1,1,1,2,3,3]
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)

# Example 3
nums = [-1,0,0,0,0,3,3]
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)

# Runtime
# Details
# 71ms
# Beats 7.23%of users with Python3
# Memory
# Details
# 16.19MB
# Beats 88.69%of users with Python3