// 128. Longest Consecutive Sequence
// Solved
// Medium
// Topics
// premium lock icon
// Companies
// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

// Example 1:

// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
// Example 2:

// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9
// Example 3:

// Input: nums = [1,0,1,2]
// Output: 3

// Constraints:

// 0 <= nums.length <= 105
// -109 <= nums[i] <= 109

package main

// HashSet, check with set if there's a number before and after in set
// O(n), O(n)
func longestConsecutive(nums []int) int {
	numSet := make(map[int]struct{})
	longest := 0
	for _, num := range nums {
		numSet[num] = struct{}{}
	}

	for num := range numSet {
		// check if it's the start of a sequence, update longest
		if _, found := numSet[num-1]; !found {
			length := 1
			for {
				if _, exists := numSet[num+length]; exists {
					length++
				} else {
					break
				}
			}
			if length > longest {
				longest = length
			}
		}
	}
	return longest
}
