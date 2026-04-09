# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        dummy2 = ListNode(0)
        tail2 = dummy2
        cur = head

        while cur:
            if cur.val < x:
                tail.next = cur
                tail = tail.next
            else:
                tail2.next = cur
                tail2 = tail2.next
            cur = cur.next
        
        tail2.next = None
        tail.next = dummy2.next

        return dummy.next
