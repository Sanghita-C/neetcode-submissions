# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Questions: 
        - any memory constraint ? do inplace
        - empty node ? yes
        
        algorithm : 

        [ 0 -> 1 -> 2 -> 3].     
          
        ps  [3 2 1 0 null]
        temp = [null]
        pv= [3 2 1 0 null]

        steps: 

        temp = ps.next
        ps.next = pv
        pv = ps
        ps = temp

        

        

        """

        if head is None: 
            return None
        
        prev = None
        present = head

        while present is not None:
            temp = present.next
            present.next = prev
            prev = present
            present = temp
        
        return prev