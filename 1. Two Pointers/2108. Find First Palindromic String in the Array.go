// 2108. Find First Palindromic String in the Array
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Hint
// Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

// A string is palindromic if it reads the same forward and backward.

// Example 1:

// Input: words = ["abc","car","ada","racecar","cool"]
// Output: "ada"
// Explanation: The first string that is palindromic is "ada".
// Note that "racecar" is also palindromic, but it is not the first.
// Example 2:

// Input: words = ["notapalindrome","racecar"]
// Output: "racecar"
// Explanation: The first and only string that is palindromic is "racecar".
// Example 3:

// Input: words = ["def","ghi"]
// Output: ""
// Explanation: There are no palindromic strings, so the empty string is returned.

// Constraints:

// 1 <= words.length <= 100
// 1 <= words[i].length <= 100
// words[i] consists only of lowercase English letters.

package main

// 2 pointers
// O(n*m), O(1)
func firstPalindrome(words []string) string {
	for _, str := range words {
		l, r := 0, len(str)-1
		isPal := true
		for l < r {
			if rune(str[l]) != rune(str[r]) {
				isPal = false
				break
			}
			l++
			r--
		}
		if isPal {
			return str
		}
	}
	return ""
}

func firstPalindrome2(words []string) string {
	for _, word := range words {
		left, right := 0, len(word)-1
		for left < right && word[left] == word[right] {
			left++
			right--
		}
		if left >= right {
			return word
		}
	}
	return ""
}
