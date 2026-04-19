# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        
        width = length // k 
        rem = length % k
        
        res = []
        curr = head
        
        for i in range(k):
            base = curr
            for j in range(width + (i < rem) - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                temp = curr.next
                curr.next = None 
                curr = temp
            
            res.append(base)
            
        return res
