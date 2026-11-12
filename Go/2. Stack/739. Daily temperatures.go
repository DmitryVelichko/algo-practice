// 739. Daily Temperatures
// Solved
// Medium
// Topics
// premium lock icon
// Companies
// Hint
// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

// Example 1:

// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]
// Example 2:

// Input: temperatures = [30,40,50,60]
// Output: [1,1,1,0]
// Example 3:

// Input: temperatures = [30,60,90]
// Output: [1,1,0]

// Constraints:

// 1 <= temperatures.length <= 105
// 30 <= temperatures[i] <= 100

package main

// Stack, array of zeroes, if current temperature > temperature in stack, pop stackIndex from stack
// and push (i minus stackIndex) to res[stackIndex], append current index to stack on each iteration
// O(n), O(n)
func dailyTemperatures(temps []int) []int {
	res := make([]int, len(temps))
	stack := []int{}

	for i, t := range temps {
		for len(stack) > 0 && t > temps[stack[len(stack)-1]] {
			stackIndx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[stackIndx] = i - stackIndx
		}
		stack = append(stack, i)
	}
	return res
}
