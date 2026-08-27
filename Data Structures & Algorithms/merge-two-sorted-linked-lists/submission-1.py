# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1 = []

        
        l2 = [4]

        h = [1 1 2, 3, 4]  []
                       p
        head = Null
        prev = Null 

        l1.val > l2.val: 
            head == null: 
                head = l2.head
                next = l2.next
                prev = head
                prev.next = null
                l2 = next

            head != null
                prev.next = l2
                next = l2.next
                prev = prev.next
                prev.next = null
                l2 = next


        l1.val <= l2.val:

            head == null: 
                head = l1.head
                next = l1.next
                prev = head
                prev.next = null
                l1 = next

            head != null: 
                prev.next = l1
                next = l1.next
                prev = prev.next
                prev.next = null
                l1 = next


        """
        if l1 == None and l2 == None: 
            return None

        if l1 == None: 
            return l2
        if l2 == None:
            return l1
        
        head = None
        prev = None

        while l1 != None and l2 != None:
            if l1.val > l2.val: 
                if head == None: 
                    head = l2
                    temp = l2.next
                    prev = l2
                    prev.next = None
                    l2 = temp

                else:
                    prev.next = l2
                    temp = l2.next
                    prev = l2
                    prev.next = None
                    l2 = temp
            else:
                if head == None: 
                    head = l1
                    temp = l1.next
                    prev = head
                    prev.next = None
                    l1 = temp

                else: 
                    prev.next = l1
                    temp = l1.next
                    prev = prev.next
                    prev.next = None
                    l1 = temp

        if l1 is not None:
            prev.next = l1
        if l2 is not None:
            prev.next = l2

        return head

        