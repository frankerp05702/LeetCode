from typing import Optional
import collections

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def create_random_linked_list(self, head):
        prev = None
        n = len(head)
        index_map = collections.defaultdict()
        for i in range(n - 1, -1, -1):
            val, random_index = head[i]
            lnode = Node(val, prev, random_index)
            index_map[i] = lnode
            if i < n - 1:
                lnode.next = prev
            prev = lnode
        
        lnode = prev
        while lnode:
            lnode.random = index_map[lnode.random] if lnode.random != None else None
            lnode = lnode.next
        
        return self.copyRandomList(prev)
           
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = Node(0)
        dummy = curr
        index_map = collections.defaultdict()

        while head:
            curr.next = Node(head.val, None, head.random)
            index_map[head] = curr.next
            curr = curr.next
            head = head.next

        curr = dummy.next
        while curr:
            if curr.random: curr.random = index_map[curr.random]
            curr = curr.next

        return dummy.next


# Example 1
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
expected = [[7,None],[13,0],[11,4],[10,2],[1,0]]
s = Solution()
copied = s.create_random_linked_list(head)
result = []
while copied:
    result.append(list((copied.val, copied.random)))
    copied = copied.next
print(result)
print(result == expected)


# Example 2:
head = [[1,1],[2,1]]
expected = [[1,1],[2,1]]
s = Solution()
copied = s.create_random_linked_list(head)
result = []
while copied:
    result.append(list((copied.val, copied.random)))
    copied = copied.next
print(result)
print(result == expected)

# Example 3:
head = [[3,None],[3,0],[3,None]]
expected = [[3,None],[3,0],[3,None]]
s = Solution()
copied = s.create_random_linked_list(head)
result = []
while copied:
    result.append(list((copied.val, copied.random)))
    copied = copied.next
print(result)
print(result == expected)
