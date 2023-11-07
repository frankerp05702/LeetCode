from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rep={}
        # Initialize dictionary
        for num in nums:
            rep[num]=nums.count(num)

        # Remove repetitions
        for key in rep.keys():
            occurrences = rep[key]
            if occurrences>1:
                for i in range(occurrences-1):
                    nums.remove(key)

        return len(nums)


# Example 1:
nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)

# Example 2:
nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
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
# 6150ms
# Beats 5.04%of users with Python3
# Memory
# Details
# 17.73MB
# Beats 78.92%of users with Python3