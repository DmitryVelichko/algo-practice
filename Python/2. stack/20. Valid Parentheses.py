# 20. Valid Parentheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Stack, push opposite bracket to stack, closing bracket must equal the top bracket popped from stack, stack must be empty
# O(n), O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if(char == "("): stack.append(")")
            elif(char == "["): stack.append("]")
            elif(char == "{"): stack.append("}")
            elif not stack or char != stack.pop(): return False
        return len(stack) == 0