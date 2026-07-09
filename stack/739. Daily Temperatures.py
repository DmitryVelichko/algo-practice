# 739. Daily Temperatures
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

# Stack, array of zeroes, if greater temperature pop index from stack and push i-index to res[index], append index to stack on each iteration
# O(n), O(n)
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)
        for i in range(len(temps)):
            while stack and temps[i] > temps[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
        