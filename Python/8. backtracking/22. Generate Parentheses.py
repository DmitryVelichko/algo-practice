# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8
 
# Backtracking:
# 1 if open == close == n, then we can append string to result
# 2 if open < n add (
# 3 if open > close add )
# O(2^n), O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, close, strng):
            if open == close == n:
                res.append(strng)
                return
            if n > open:
                backtrack(open + 1, close, strng + "(")
            if open > close:
                backtrack(open, close + 1, strng + ")")

        backtrack(0, 0, "")
        return res
