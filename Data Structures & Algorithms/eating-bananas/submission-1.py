class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Eating Rate
        k_min = 1
        k_max = max(piles)
        k = k_max

        # Now that we have our search area lets find the minimum eating rate 
        while k_min <= k_max:
            m = (k_min + k_max) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile/m)

            if time > h:
                k_min = m + 1
            elif time <= h:
                k = min(k,m)
                k_max = m - 1

        return k
