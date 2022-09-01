# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode(-1)
        carry = 0
        
        while l1 or l2 or carry == 1:
            tmp_sum = 0
            if l1:
                tmp_sum += l1.val
                l1 = l1.next
            if l2:
                tmp_sum += l2.val
                l2 = l2.next
            tmp_sum += carry
            if tmp_sum >= 10:
                carry = 1
                curr.next = ListNode(tmp_sum - 10)
                curr = curr.next
            else:
                carry = 0
                curr.next = ListNode(tmp_sum)
                curr = curr.next
                
        return head.next