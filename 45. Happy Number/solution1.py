class Solution:
    def isHappy(self, n: int) -> bool:
        prev = set()

        while n < 2**31 - 1:
            digits = list(map(int, str(n)))
            n = 0
            for num in digits:
                n += num**2
            if n == 1:
                return True
            if n in prev: return False
            prev.add(n)
                
        return False

# Example 1:
n = 19
# Output: true
s = Solution()
result = s.isHappy(n)
print(result)
print(result == True)


# Example 2:
n = 2
# Output: false
s = Solution()
result = s.isHappy(n)
print(result)
print(result == False)