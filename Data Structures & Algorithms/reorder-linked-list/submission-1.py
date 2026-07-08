# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        [0, 1, 2, 3, 4, 5, 6]
                  sp
                           fp
        step 1 - create the new head o(n)
        h -> [0,1,2,3]
        nh -> [4,5,6]
        step 2 - reverse the new linked list o(n)
        nh-> [6,5,4]
        step3 -> merging the two lists



        [0, 1, 2, 3, 4 , 5]= [0, 5,1,4,2,3]
               sp
                     fp
        """
        # creating the two linkedlists
        slow_pointer, fast_pointer = head, head

        while fast_pointer and fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        newhead = slow_pointer.next
        slow_pointer.next = None
        
        # check cases when newhead is null 
        #print(f"newhead starts at{newhead.val}")

        #reverse newhead
        prev = None
        
        while newhead and newhead.next:
            nexthead = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = nexthead
        
        if newhead:
            newhead.next = prev
        else:
            return 
        #print(f"reversed list starts at {newhead.val}")
        
        #merging
        """
        h -> [0,4, 1,5, 2,6, 3].       final [0,4,1,2,3]
                             s

        nh -> []
               nh

        h -> [0,3, 1,4, 2, 5]
                            s

        nh -> []
               nh

        """
        
        start = head
        while newhead and start:
            #print(f"original list node is {start.val} and newhead is {newhead.val}")
            original_next = start.next
            reverse_list_next = newhead.next
            newhead.next = None
            start.next = newhead
            newhead.next = original_next
            newhead = reverse_list_next
            start = original_next
        
        
        return




        