class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorting Method

        return sorted(s) == sorted(t)
