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
    
# Encode and Decode Strings
# Medium
# Topics
# Company Tags
# Hints
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }
# So Machine 1 does:

# String encoded_string = encode(strs);
# and Machine 2 does:

# List<String> decoded_strs = decode(encoded_string);
# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: strs = ["Hello","World"]

# Output: ["Hello","World"]
# Explanation:

# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

# // Machine 1 ---encoded_string---> Machine 2

# List<String> decoded_strs = solution.decode(encoded_string);

# Example 2:

# Input: strs = [""]

# Output: [""]

# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Follow up: Could you write a generalized algorithm to work on any possible set of characters?

# O(m+n), O(m+n)
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# check with set if there's a number before and after in set
# O(n), O(n)
