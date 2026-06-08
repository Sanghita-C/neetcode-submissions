# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        l1,l2 = list1, list2
        head = l1 if l1.val <= l2.val else l2
        if head == l1: 
            l1 = l1.next
            
        else:
            l2 = l2.next

        prev = head
            

        

        while l1!= None and l2!= None:
            if l1.val <= l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
                prev.next =None

            else: 
                prev.next = l2
                prev = l2
                l2 = l2.next
                prev.next = None

        if l1 != None:
            prev.next = l1
        if l2 !=None : 
            prev.next = l2

        return head



    


        