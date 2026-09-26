// 1768. Merge Strings Alternately
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Hint
// You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

// Return the merged string.

// Example 1:

// Input: word1 = "abc", word2 = "pqr"
// Output: "apbqcr"
// Explanation: The merged string will be merged as so:
// word1:  a   b   c
// word2:    p   q   r
// merged: a p b q c r
// Example 2:

// Input: word1 = "ab", word2 = "pqrs"
// Output: "apbqrs"
// Explanation: Notice that as word2 is longer, "rs" is appended to the end.
// word1:  a   b
// word2:    p   q   r   s
// merged: a p b q   r   s
// Example 3:

// Input: word1 = "abcd", word2 = "pq"
// Output: "apbqcd"
// Explanation: Notice that as word1 is longer, "cd" is appended to the end.
// word1:  a   b   c   d
// word2:    p   q
// merged: a p b q c   d

// Constraints:

// 1 <= word1.length, word2.length <= 100
// word1 and word2 consist of lowercase English letters.

package main

// O(n+m), O(n+m): n,m = length of w1 and w2 strings
func mergeAlternately(word1 string, word2 string) string {
	res := make([]byte, 0, len(word1)+len(word2))
	i, j := 0, 0

	for i < len(word1) && j < len(word2) {
		res = append(res, word1[i])
		res = append(res, word2[j])
		i++
		j++
	}
	res = append(res, word1[i:]...)
	res = append(res, word2[j:]...)

	return string(res)
}

func mergeAlternately2(word1 string, word2 string) string {
	n, m := len(word1), len(word2)
	var res strings.Builder

	maxLen := n
	if m > maxLen {
		maxLen = m
	}

	for i := 0; i < maxLen; i++ {
		if i < n {
			res.WriteByte(word1[i])
		}
		if i < m {
			res.WriteByte(word2[i])
		}
	}
	return res.String()
}
