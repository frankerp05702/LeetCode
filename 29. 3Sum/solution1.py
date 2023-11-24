from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum < 0:
                    j += 1
                elif current_sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1; k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return result



# Example 1:
nums = [-1,0,1,2,-1,-4]
expected = [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
s = Solution()
result = s.threeSum(nums)
print(result)
print(result == expected)


# Example 2:
nums = [0,1,1]
expected = []
# Explanation: The only possible triplet does not sum up to 0.
s = Solution()
result = s.threeSum(nums)
print(result)
print(result == expected)


# Example 3:
nums = [0,0,0]
expected = [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
s = Solution()
result = s.threeSum(nums)
print(result)
print(result == expected)

# Example 4:
nums = [-1,0,1]
expected = [-1,0,1]
# Explanation: The only possible triplet sums up to 0.
s = Solution()
result = s.threeSum(nums)
print(result)
print(result == expected)