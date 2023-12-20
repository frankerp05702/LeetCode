from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def create_simply_linked_lists(self, head, ith):
        prev = None
        n = len(head)
        for i in range(n - 1, -1, -1):
            lnode = ListNode(head[i])
            if i < n - 1:
                lnode.next = prev
            # if i + 1 == left: left = lnode
            # elif i + 1 == right: right = lnode
            prev = lnode
        return self.removeNthFromEnd(prev, ith)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        list = []
        while head:
            list.append(head)
            head = head.next

        m = len(list)

        if m == 0 or m < n or n < 0: return start

        pos = m - n
        if pos < 0 or pos > m - 1:
            return start
        
        if pos == 0:
            start = list[pos + 1] if pos != m - 1 else None
        else:
            list[pos - 1].next = list[pos + 1] if pos != m - 1 else None
        
        return start


# Example 1:
head = [1,2,3,4,5]
n = 2
expected = [1,2,3,5]
s = Solution()
remain = s.create_simply_linked_lists(head, n)
result = []
while remain:
    result.append(remain.val)
    remain = remain.next
print(result)
print(result == expected)


# Example 2:
head = [1]
n = 1
expected = []
s = Solution()
remain = s.create_simply_linked_lists(head, n)
result = []
while remain:
    result.append(remain.val)
    remain = remain.next
print(result)
print(result == expected)

# Example 3:
head = [1,2]
n = 1
expected = [1]
s = Solution()
remain = s.create_simply_linked_lists(head, n)
result = []
while remain:
    result.append(remain.val)
    remain = remain.next
print(result)
print(result == expected)