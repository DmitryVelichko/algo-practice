// 242. Valid Anagram
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// Example 1:

// Input: s = "anagram", t = "nagaram"

// Output: true

// Example 2:

// Input: s = "rat", t = "car"

// Output: false

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

// Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

package main

// Hasmap, map runes and frequency("a": 0++ and "a": 0--), must be all 0s.
// O(n), O(n+k) - n coz of rune slices and map, k = number of distinct chars, supports unicode chars
func isAnagram(s string, t string) bool {
	sRunes := []rune(s)
	tRunes := []rune(t)

	if len(sRunes) != len(tRunes) {
		return false
	}
	hash := make(map[rune]int)
	for i := range sRunes {
		hash[sRunes[i]]++
		hash[tRunes[i]]--
	}

	for key := range hash {
		if hash[key] != 0 {
			return false
		}
	}
	return true
}
