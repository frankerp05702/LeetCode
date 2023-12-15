from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def create_simply_linked_lists(self, l1, l2):
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
        
        return self.mergeTwoLists(prev, prev2)
           
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        merged = dummy

        while list1 or list2:
            if not list2:
                merged.next = ListNode(list1.val)
                list1 = list1.next
            elif not list1:
                merged.next = ListNode(list2.val)
                list2 = list2.next
            else:
                if list1.val <= list2.val:
                    merged.next = ListNode(list1.val)
                    list1 = list1.next
                elif list1.val > list2.val:
                    merged.next = ListNode(list2.val)
                    list2 = list2.next
            merged = merged.next

        return dummy.next


# Example 1
list1 = [1,2,4]
list2 = [1,3,4]
expected = [1,1,2,3,4,4]
s = Solution()
merged = s.create_simply_linked_lists(list1, list2)
result = []
while merged:
    result.append(merged.val)
    merged = merged.next
print(result)
print(result == expected)


# Example 2:
list1 = []
list2 = []
expected = []
s = Solution()
merged = s.create_simply_linked_lists(list1, list2)
result = []
while merged:
    result.append(merged.val)
    merged = merged.next
print(result)
print(result == expected)

# Example 3:
list1 = []
list2 = [0]
expected = [0]
s = Solution()
merged = s.create_simply_linked_lists(list1, list2)
result = []
while merged:
    result.append(merged.val)
    merged = merged.next
print(result)
print(result == expected)
