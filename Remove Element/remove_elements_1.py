from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dec_indx = len(nums)-1
        for i,num in enumerate(nums):
            if num==val:
                filler='a'
                for j in range(dec_indx,i,-1):
                    if nums[j]!=val:
                        filler=nums.pop(j)
                        dec_indx=j-1
                        break
                if filler!='a':
                    nums[i]=filler
                else:
                    for x in range(len(nums)-1,i,-1):
                        nums.pop(x)
                    nums.pop(i)
        return len(nums)


# Example 1
nums = [3,2,2,3]
val = 3
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

# Example 2
nums = [0,1,2,2,3,0,4,2]
val = 2
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

# #Example 3
nums = [2]
val = 3
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

#Example 4
nums = [1]
val = 1
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

#Example 5
nums = [3,3]
val = 3
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

# Runtime
# Details
# 32ms
# Beats 94.57%of users with Python3
# Memory
# Details
# 16.35MB
# Beats 9.20%of users with Python3