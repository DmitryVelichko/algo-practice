# 242. Valid Anagram
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# O(n), O(26 english letters) => O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        for i in count.values():
            if i != 0:
                return False
        return True
    

    # Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    #  The biggest issue with Unicode in anagram problems is that the same visual character can be represented in multiple ways in memory.
     # Normalize both strings to NFC format (canonical composition)
        # s = unicodedata.normalize("NFC", s) in memory