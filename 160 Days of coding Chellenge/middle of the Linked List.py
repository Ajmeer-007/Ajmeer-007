# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.length_cal(head)

        mid = length//2
        while(mid):
            head = head.next
            mid -=1
        return head

    def length_cal(self,head):
        length = 0
        while(head):
            length+=1
            head = head.next
        return length
        
