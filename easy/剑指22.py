# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        len = 1
        ans = ListNode(head.val)
        endNode = ans
        tar = head.next

        while len < k:
            endNode.next = ListNode(tar.val)
            endNode = endNode.next
            tar = tar.next
            len += 1

        while tar != None:
            ans = ans.next
            endNode.next = ListNode(tar.val)
            endNode = endNode.next
            tar = tar.next
        
        return ans

