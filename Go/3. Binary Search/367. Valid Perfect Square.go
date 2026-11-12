// 367. Valid Perfect Square
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Given a positive integer num, return true if num is a perfect square or false otherwise.

// A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

// You must not use any built-in library function, such as sqrt.

// Example 1:

// Input: num = 16
// Output: true
// Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
// Example 2:

// Input: num = 14
// Output: false
// Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

// Constraints:

// 1 <= num <= 231 - 1

package main

// Binary search
// O(log n), O(1)
func isPerfectSquare(num int) bool {
	l, r := 1, num

	for l <= r {
		m := l + (r-l)/2
		sq := m * m
		if sq > num {
			r = m - 1
		} else if sq < num {
			l = m + 1
		} else {
			return true
		}
	}

	return false
}

// O(sqrt(n)), O(1)
func isPerfectSquare2(num int) bool {
	i := 1
	for num > 0 {
		num -= i
		i += 2
	}
	return num == 0
}
