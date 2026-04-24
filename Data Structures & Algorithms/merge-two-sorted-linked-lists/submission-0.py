# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curr = None
        if list1 is not None:
            if list2 is not None:
                if list1.val <= list2.val:
                    new_head = list1
                    list1 = list1.next
                else:
                    new_head = list2
                    list2 = list2.next
            else:
                return list1
        else:
            return list2

        curr_pointer = new_head
        while list1 is not None:
            if list2 is not None:
                if list1.val <= list2.val:
                    curr_pointer.next = list1
                    curr_pointer = list1
                    list1 = list1.next
                    print('list1')
                else:
                    curr_pointer.next = list2
                    curr_pointer = list2
                    list2 = list2.next
                    print('list2')
            else:
                # Add the rest of list1
                curr_pointer.next = list1
                break

        if list2 is not None:
            # Add the rest of list2
            curr_pointer.next = list2

        return new_head