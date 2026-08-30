# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        - Are these unique numbers ? No
        - length of list ? max 1000 -but it is not given

        Algorithm :

        slow - moves one step ahead
        fast -moves two steps ahead

        if fast = slow at some point return True
        if fast reaches null then return false
        """
        if head is None:
            return False

        slow = head.next #2
        if slow:
            fast = slow.next #1
        else:
            return False


        while fast is not None and fast.next is not None and fast.next.next is not None:
            #print(f"fast and slow vals are: {fast.val} and {slow.val}")
            if slow == fast:
                return True
            
            slow = slow.next #1
            fast = fast.next #2
            if fast.next:
                fast = fast.next #1
        

        return False

        