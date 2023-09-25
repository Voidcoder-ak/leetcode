class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() 
        nlist = dummy

        while list1 and list2:
            if list1.val < list2.val:
                nlist.next = list1
                list1 = list1.next
            else:
                nlist.next = list2
                list2 = list2.next
            nlist = nlist.next

        if list1:
            nlist.next = list1
        elif list2:
            nlist.next = list2