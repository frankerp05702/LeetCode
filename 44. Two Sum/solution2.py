from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = []
            nums_dict[nums[i]].append(i)
        
        nums_upd = sorted(list(set(nums)))

        for i in range(len(nums_upd)):
            el = nums_upd[i]

            if el == target // 2 and len(nums_dict[el]) > 1:
                return [nums_dict[el][0], nums_dict[el][1]]

            l, r = i + 1, len(nums_upd)
            while r - l > 1:
                m = (l + r) // 2
                if nums_upd[m] > target - el:
                    r = m
                else:
                    l = m
            
            if nums_upd[l] == target - nums_upd[i]:
                ind1 = nums_dict[el][0]
                ind2 = nums_dict[nums_upd[l]][0]
                return [ind1, ind2]



# Example 1:
nums = [2,7,11,15]
target = 9
expected = [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 2:
nums = [3,2,4]
target = 6
expected = [1,2]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 3:
nums = [3,3]
target = 6
expected = [0,1]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 4:
nums = [3,2,3]
target = 6
expected = [0,2]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 5:
nums = [2,5,5,11]
target = 10
expected = [1,2]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 6:
nums = [0,4,3,0]
target = 0
expected = [0,3]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)