package main

// Hashmap one pass, complement pair
// O(n), O(n)
func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		if index, found := hash[complement]; found {
			return []int{index, i}
		}
		hash[num] = i
	}
	return []int{}
}
