class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tmp = ','.join(sorted(s))
            res[tmp].append(s)
        return list(res.values())