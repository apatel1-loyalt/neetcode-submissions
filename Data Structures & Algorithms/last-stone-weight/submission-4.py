class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # We are using Min heap solutions
        # Converting stones value to negative
        stones = [-s for s in stones]

        # Converting stones to heapify 
        heapq.heapify(stones)

        # lopping while list have any two memebers
        while len(stones) >= 2:
            # First memeber is the smallest negaive meaning largest positive
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first-second)

        # if the stones list is empty we add the 0 as the default answer
        stones.append(0)

        return abs(stones[0])