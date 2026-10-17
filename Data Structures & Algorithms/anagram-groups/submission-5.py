class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """OP Solution"""

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # For a - z chars

            for c in s:
                count[(ord(c)-ord('a'))] += 1  # To get asci value of charactors and create a 26 index count

            res[tuple(count)].append(s)

        return list(res.values())

