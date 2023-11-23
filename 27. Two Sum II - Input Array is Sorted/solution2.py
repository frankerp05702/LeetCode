from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        start = n - 1
        while i < n - 1:
            for j in range(start, i, -1):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                if numbers[i] + numbers[j] < target:
                    start = j
                    break
            for i in range(i, j):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                if numbers[i] + numbers[j] > target:
                    break
            

# Example 1:

numbers = [2,7,11,15]
target = 9
expected = [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
s = Solution()
result = s.twoSum(numbers, target)
print(result)
print(result == expected)


# Example 2:

numbers = [2,3,4]
target = 6
expected = [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
s = Solution()
result = s.twoSum(numbers, target)
print(result)
print(result == expected)

# Example 3:

numbers = [-1,0]
target = -1
expected = [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
s = Solution()
result = s.twoSum(numbers, target)
print(result)
print(result == expected)