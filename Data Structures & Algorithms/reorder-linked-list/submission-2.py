# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            # slow ends up at end of first half of linked list
            slow = slow.next
            fast = fast.next.next

        # Make sure list ends with None
        temp = slow.next
        slow.next = None
        slow = temp

        # Reverse second half of linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # Now, prev is the new head of the reversed second half

        # Reset fast pointer to start
        fast = head
        slow = prev
        while slow:
            temp = fast.next
            fast.next = slow
            fast = temp

            temp = slow.next
            slow.next = fast
            slow = temp
