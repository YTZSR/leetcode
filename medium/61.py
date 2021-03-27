# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
            
        temp = head
        len = 1
        while temp.next:
            temp = temp.next
            len += 1
        
        k = k % len
        if k == 0:
            return head
        
        temp.next = head
        
        for i in range(len - k):
            temp = temp.next
        ans = temp.next
        temp.next = None
        return ans
