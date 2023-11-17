from typing import List
from math import trunc

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        kids = [1]*n

        if n<2: return n

        for i in range(1, n):
            if ratings[i]>ratings[i-1]:
                kids[i] = kids[i-1] + 1

        for i in range(i-1, -1, -1):
            if ratings[i]>ratings[i+1]:
                if kids[i] <= kids[i+1]: 
                    kids[i] = kids[i+1] + 1

        return sum(kids)

# Example 1:

ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
s=Solution()
response = s.candy(ratings)
print(response)
print(response==5)

# Example 2:

ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
s=Solution()
response = s.candy(ratings)
print(response)
print(response==4)

ratings = [1,3,2,2,1]
s=Solution()
response = s.candy(ratings)
print(response)
print(response==7)

ratings = [1,2,87,87,87,2,1]
# Output: 13
s=Solution()
response = s.candy(ratings)
print(response)
print(response==13)

ratings = [29,51,87,87,72,12]
# Output: 12
s=Solution()
response = s.candy(ratings)
print(response)
print(response==12)

ratings = [1,3,4,5,2]
# Output: 11
s=Solution()
response = s.candy(ratings)
print(response)
print(response==11)

ratings = [0,1,2,3,2,1]
# Output: 13
s=Solution()
response = s.candy(ratings)
print(response)
print(response==13)

ratings = [1,6,10,8,7,3,2]
# Output: 18
s=Solution()
response = s.candy(ratings)
print(response)
print(response==18)

ratings = [0,1,2,5,3,2,7]
# Output: 15
s=Solution()
response = s.candy(ratings)
print(response)
print(response==15)

ratings = [1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]
# Output: 47
s=Solution()
response = s.candy(ratings)
print(response)
print(response==47)

ratings = [10,10,10,10,10,10]
# Output: 6
s=Solution()
response = s.candy(ratings)
print(response)
print(response==6)

ratings = [2,2]
# Output: 2
s=Solution()
response = s.candy(ratings)
print(response)
print(response==2)

ratings = [2,2,1]
# Output: 4
s=Solution()
response = s.candy(ratings)
print(response)
print(response==4)

ratings = [58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89]
# Output: 208
s=Solution()
response = s.candy(ratings)
print(response)
print(response==208)