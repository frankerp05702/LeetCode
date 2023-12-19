from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def create_simply_linked_lists(self, head, k):
        prev = None
        n = len(head)
        for i in range(n - 1, -1, -1):
            lnode = ListNode(head[i])
            if i < n - 1:
                lnode.next = prev
            # if i + 1 == left: left = lnode
            # elif i + 1 == right: right = lnode
            prev = lnode
        return self.reverseKGroup(prev, k)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        count = 1
        left_prev, right_next, prev = None, None, None
        
        if left == right: return head
        
        while head:
            head_next = head.next
            if count == left - 1:
                left_prev = head
            elif count == left:
                prev = left_node = head
            elif count > left and count <= right:
                if count == right:
                    right_node = head
                # My Next is my prev
                head.next = prev
                prev = head
            elif count == right + 1:
                right_next = head
                break
            head = head_next
            count += 1
        
        if left_prev: left_prev.next = right_node
        left_node.next = right_next

        if left == 1: start = right_node
        return start
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 1
        start = lap_start = head
        lap_start_prev = None

        if k == 1: return head

        while head:
            head_next = head.next
            if counter % k == 0:
                reversed = self.reverseBetween(lap_start, 1, k)
                if lap_start == start: start = reversed
                if lap_start_prev: 
                    lap_start_prev.next = reversed
                lap_start_prev = lap_start
                lap_start = head_next
            head = head_next
            counter += 1
        
        return start


# Example 1:
head = [1,2,3,4,5]
k = 2
expected = [2,1,4,3,5]
s = Solution()
reversed = s.create_simply_linked_lists(head, k)
result = []
while reversed:
    result.append(reversed.val)
    reversed = reversed.next
print(result)
print(result == expected)


# Example 2:
head = [1,2,3,4,5]
k = 3
expected = [3,2,1,4,5]
s = Solution()
reversed = s.create_simply_linked_lists(head, k)
result = []
while reversed:
    result.append(reversed.val)
    reversed = reversed.next
print(result)
print(result == expected)

# Example 3:
head = [1,2,3,4,5,6]
k = 3
expected = [3,2,1,6,5,4]
s = Solution()
reversed = s.create_simply_linked_lists(head, k)
result = []
while reversed:
    result.append(reversed.val)
    reversed = reversed.next
print(result)
print(result == expected)