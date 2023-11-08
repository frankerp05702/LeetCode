from typing import List

class Solution:
    # Swap two elements given the List and indexes of each
    def swap(self, nums: List[int], i: int, j: int)->None:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp

    # Revert complete array
    def revert(self, nums: List[int], i: int, j: int):
        while i<j:
            self.swap(nums,i,j)
            i+=1
            j-=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<0: return

        start=len(nums)-k
        while start<0:
            start+=len(nums)
        end=len(nums)-1
        self.revert(nums,start,end)
        end=start-1
        start=0
        self.revert(nums,start,end)
        end=len(nums)-1
        start=0
        self.revert(nums,start,end)

    
# Example 1:
nums = [1,2,3,4,5,6,7]
k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
s = Solution()
s.rotate(nums, k)
print(nums)

# Example 2:
nums = [-1,-100,3,99]
k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
s = Solution()
s.rotate(nums, k)
print(nums)

# Example 3:
nums = [1,2,3]
k = 4
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
s = Solution()
s.rotate(nums, k)
print(nums)


# Runtime
# Details
# 180ms
# Beats 71.21%of users with Python3
# Memory
# Details
# 27.80MB
# Beats 43.34%of users with Python3