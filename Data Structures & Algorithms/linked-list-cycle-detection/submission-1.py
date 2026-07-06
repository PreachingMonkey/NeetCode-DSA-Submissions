# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head==None or head.next == None:
            return False
        if head.val == 'v':
            return True
        else:
            head.val = 'v'
        return self.hasCycle(head.next)