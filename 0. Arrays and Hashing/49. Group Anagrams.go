// 49. Group Anagrams
// Solved
// Medium
// Topics
// premium lock icon
// Companies
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]

// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Explanation:

// There is no string in strs that can be rearranged to form "bat".
// The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
// The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
// Example 2:

// Input: strs = [""]

// Output: [[""]]

// Example 3:

// Input: strs = ["a"]

// Output: [["a"]]

// Constraints:

// 1 <= strs.length <= 104
// 0 <= strs[i].length <= 100
// strs[i] consists of lowercase English letters.

package main

// O(n * k), n - number of strs, k - length of the longest string, O(n*k) - coz of hasmap of arrays
// Frequency array of 26 chars: [0++,1++,0++...], hashamp {"1110...": ["bac", "cab"]}
func groupAnagrams(strs []string) [][]string {
	hash := make(map[[26]int][]string)

	for _, str := range strs {
		var freqArr [26]int
		for _, char := range str {
			freqArr[char-'a']++
		}
		hash[freqArr] = append(hash[freqArr], str)
	}

	var result [][]string
	for _, group := range hash {
		result = append(result, group)
	}
	return result
}
