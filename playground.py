# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Dummy and tail nodes, append node with smaller val to tail, when one list becomes empty - append the whole other list, return dummy.next
# O(n+m) - n & m is the length of l1 & l2, O(1) space - we reuse the existing nodes
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1: tail.next = l1
        if l2: tail.next = l2
        return dummy.next
        