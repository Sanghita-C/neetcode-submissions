# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        <1 <2<3<4 <5
                  H
        
P=None.         P
        1-> 2 :  2->1: head -> 2> 1 :: 3-> 4->5
        """

        if not head:
            return None
        

        Prev = None

        while head.next: 
            new_head = head.next
            head.next = Prev
            Prev = head
            head = new_head
        
        head.next = Prev

        return head

        

        