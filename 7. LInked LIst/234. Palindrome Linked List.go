// 234. Palindrome Linked List
// Easy
// Topics
// premium lock icon
// Companies
// Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

// Example 1:

// Input: head = [1,2,2,1]
// Output: true
// Example 2:

// Input: head = [1,2]
// Output: false

// Constraints:

// The number of nodes in the list is in the range [1, 105].
// 0 <= Node.val <= 9

// Follow up: Could you do it in O(n) time and O(1) space?

package main
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// Fast and slow pointers, reverse second half of linked list, check palindrome
// O(n), O(1)
func isPalindrome(head *ListNode) bool {
    fast, slow := head, head

    // find middle (slow)
    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
    }

    // reverse second half
    var prev *ListNode
    for slow != nil {
        tmp := slow.Next
        slow.Next = prev
        prev = slow
        slow = tmp
    }

