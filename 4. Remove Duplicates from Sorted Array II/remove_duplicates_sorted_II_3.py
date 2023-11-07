from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=None
        freq=0
        pos=0
        temp=[num for num in nums]
        # As numbers are ordered
        for num in temp:
            if num!=prev:
                freq=1
                nums[pos]=num
                prev=num
                pos+=1
            else:
                if freq<2: 
                    freq+=1
                    nums[pos]=num
                    pos+=1
                    prev=num                

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
# 52ms
# Beats 85.87%of users with Python3
# Memory
# Details
# 16.16MB
# Beats 88.69%of users with Python3