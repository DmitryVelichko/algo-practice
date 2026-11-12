// 680. Valid Palindrome II
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Given a string s, return true if the s can be palindrome after deleting at most one character from it.

// Example 1:

// Input: s = "aba"
// Output: true
// Example 2:

// Input: s = "abca"
// Output: true
// Explanation: You could delete the character 'c'.
// Example 3:

// Input: s = "abc"
// Output: false

// Constraints:

// 1 <= s.length <= 105
// s consists of lowercase English letters.

package main

// Two pointers, when mismatch (s[l] != s[r]) skip left && right character (l+1, r-1)
// and check if the rest of the string is a palindrome.
// O(n), O(1)
func validPalindrome(s string) bool {
	isPalindrome := func(l, r int) bool {
		for l < r {
			if s[l] != s[r] {
				return false
			}
			l++
			r--
		}
		return true
	}

	l, r := 0, len(s)-1
	for l < r {
		if s[l] != s[r] {
			return isPalindrome(l+1, r) || isPalindrome(l, r-1)
		}
		l++
		r--
	}

	return true
}
