package main

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	res := make([]int, 0)

	for i := 0; i < n; i++ {
		count := 1
		j := i + 1

		for j < n {
			if temperatures[j] > temperatures[i] {
				break
			}
			j++
			count++
		}

		if j == n {
			count = 0
		}

		res = append(res, count)
	}

	return res
}
