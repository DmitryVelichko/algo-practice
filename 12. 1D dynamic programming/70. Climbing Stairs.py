# 70. Climbing Stairs
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

# DP. Fibonacci, at any step, the number of ways depends only on the previous two steps. One -> ways to reach the current step, two -> ways to reach the previous step, Start both as 1 (base case). Repeat n - 1 times: new ways = one + two & shift variables forward. Return one. 
# O(n), O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one