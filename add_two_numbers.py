# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummyHead = ListNode(0)
            curr = dummyHead
            carry = 0
            p,q = l1,l2
            while p != None or q != None:
                s = carry + (p.val if p != None else 0) + (q.val if q != None else 0)
                carry = s // 10
                curr.next = ListNode(s % 10)
                curr = curr.next
                if p != None:
                    p = p.next
                if q != None:
                    q = q.next
        
            if carry > 0:
                curr.next = ListNode(carry)
        
            return dummyHead.next
            
