# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        res = 0
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        print(arr)
        n = len(arr)//2
        l = len(arr)

        for i in range(n):
            twin = l - 1 - i
            su = arr[i] + arr[twin]
            res = max(res, su)
        
        return res
