# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        cur1 = l1
        cur2 = l2

        while cur1:
            num1 += str(cur1.val)
            cur1 = cur1.next

        while cur2:
            num2 += str(cur2.val)
            cur2 = cur2.next

        num1 = num1[::-1]
        num2 = num2[::-1]

        res = int(num1) + int(num2)
        ans = str(res)[::-1]

        dummy = ListNode(0)
        current = dummy 
        
        for value in ans:
            current.next = ListNode(int(value))
            current = current.next

        return dummy.next
