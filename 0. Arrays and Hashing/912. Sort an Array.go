// 912. Sort an Array
// Attempted
// Medium
// Topics
// premium lock icon
// Companies
// Given an array of integers nums, sort the array in ascending order and return it.

// You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

// Example 1:

// Input: nums = [5,2,3,1]
// Output: [1,2,3,5]
// Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
// Example 2:

// Input: nums = [5,1,1,2,0,0]
// Output: [0,0,1,1,2,5]
// Explanation: Note that the values of nums are not necessarily unique.

package main

func sortArray(nums []int) []int {
	mergeSort(nums, 0, len(nums)-1)
	return nums
}

func mergeSort(arr []int, l, r int) {
	if l >= r {
		return
	}
	m := (l + r) / 2
	mergeSort(arr, l, m)
	mergeSort(arr, m+1, r)
	merge(arr, l, m, r)
}

func merge(arr []int, l, m, r int) {
	left := make([]int, m-l+1)
	right := make([]int, r-m)
	copy(left, arr[l:m+1])
	copy(right, arr[m+1:r+1])

	i, j, k := 0, 0, l
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			arr[k] = left[i]
			i++
		} else {
			arr[k] = right[j]
			j++
		}
		k++
	}
	for i < len(left) {
		arr[k] = left[i]
		i++
		k++
	}
	for j < len(right) {
		arr[k] = right[j]
		j++
		k++
	}
}
