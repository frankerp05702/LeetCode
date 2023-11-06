# Example 1:

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# Example 2:
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# Example 3:
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# First ApproachRuntime
# Details
# 46ms
# Beats 41.94%of users with Python3
# Memory
# Details
# 16.30MB
# Beats 59.76%of users with Python3
nums1[m:]=nums2
nums1.sort()

# Second Approach
# Runtime
# Details
# 38ms
# Beats 88.93%of users with Python3
# Memory
# Details
# 16.22MB
# Beats 59.76%of users with Python3
# i=m-1
# j=n-1
# index=m+n-1
# while i>-1 or j>-1:
#     if i==-1:
#         nums1[index]=nums2[j]
#         j-=1
#     elif j==-1:
#         nums1[index]=nums1[i]
#         i-=1 

#     if i>-1 and j>-1:
#         if nums1[i]>nums2[j]:
#             nums1[index]=nums1[i]
#             i-=1
#         else:
#             nums1[index]=nums2[j]
#             j-=1        
#     index-=1

print(nums1)