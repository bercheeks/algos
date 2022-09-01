# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mapping = {}
        count = 1
        while head:
            mapping[count] = head
            
            head = head.next
            count += 1
        remove = count - n
        if count == 2:
            return ListNode(-1).next
        if remove == 1:
            return mapping[1].next
        elif n == 1:
            mapping[remove - 1].next = None
            return mapping[1]
        else:
            mapping[remove-1].next = mapping[remove].next
            return mapping[1]