from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def create_simply_linked_lists(self, l1, l2):
        n1 = [l for l in l1]
        n2 = [l for l in l2]

        prev = None
        prev2 = None
        m = len(l1)
        for i in range(m - 1, -1, -1):
            lnode = ListNode(l1[i])
            if i < m - 1:
                lnode.next = prev
            prev = lnode
        m = len(l2)
        for i in range(m - 1, -1, -1):
            lnode = ListNode(l2[i])
            if i < m - 1:
                lnode.next = prev2
            prev2 = lnode
        
        return self.addTwoNumbers(prev, prev2)
           
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum, carrier = 0, 0
        first_node = True
        prev = None
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a + b + carrier
            if sum > 9:
                carrier = sum // 10
                sum = sum % 10
            else:
                carrier = 0
            n3 = ListNode(sum)
            if not first_node: prev.next = n3
            if first_node:
                l3 = n3
                first_node = False
            prev = n3
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
        if carrier:
            if not first_node: prev.next = ListNode(carrier)
        return l3


# Example 1
l1 = [2,4,3]
l2 = [5,6,4]
expected = [7,0,8]
# Explanation: 342 + 465 = 807.
s = Solution()
summed = s.create_simply_linked_lists(l1, l2)
result = []
while summed:
    result.append(summed.val)
    summed = summed.next
print(result)
print(result == expected)


# Example 2:
l1 = [0]
l2 = [0]
expected = [0]
s = Solution()
summed = s.create_simply_linked_lists(l1, l2)
result = []
while summed:
    result.append(summed.val)
    summed = summed.next
print(result)
print(result == expected)

# Example 3:
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
expected = [8,9,9,9,0,0,0,1]
s = Solution()
summed = s.create_simply_linked_lists(l1, l2)
result = []
while summed:
    result.append(summed.val)
    summed = summed.next
print(result)
print(result == expected)
