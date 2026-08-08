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

# 206. Reverse Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative: prev->None, curr->head, next->curr.next, break link, move prev & curr forward
# O(n), O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# Recursive O(n), O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead    