# 49. Group Anagrams
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# O(n, k), n - number of strs, k - len(str), O(n*k) - hasmap of arrays
# Create [] with 26 zeros, hashamp {010101: [strng, strng]}
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
    # O(n), O(26 english letters) => O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        for i in count:
            if count[i] != 0:
                return False
        return True
    

    # Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    #  The biggest issue with Unicode in anagram problems is that the same visual character can be represented in multiple ways in memory.
     # Normalize both strings to NFC format (canonical composition)
        # s = unicodedata.normalize("NFC", s) in memory