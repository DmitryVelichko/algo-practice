# O(n, k), n - number of strs, k - len(str), O(n*k) - hasmap of arrays
# Create [] with 26 zeros, each zero++, {010101: []}
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())