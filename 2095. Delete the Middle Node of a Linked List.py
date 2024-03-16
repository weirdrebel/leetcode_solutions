# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        # Initialize ListNode with a value and a reference to the next node
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        # If the list is empty or has only one node, return None as there's no middle node to delete
        if head is None or head.next is None:
            return None
        
        # Initialize slow and fast pointers, and a pointer to keep track of the previous node
        slow = head
        fast = head
        prev = None
        
        # Move the fast pointer twice as fast as the slow pointer
        # When the fast pointer reaches the end, the slow pointer will be at the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Connect the previous node to the next node of the middle node, effectively deleting the middle node
        prev.next = slow.next
        
        return head
