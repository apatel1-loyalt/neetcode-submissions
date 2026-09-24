class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        
        for c in t:
            if c not in count:
                return False
            elif count[c] == 0:
                return False
            else:
                count[c] -= 1
            
        return True