# Heap / Priority Queue

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            # Pop the last value if len is larger then k
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the new value to min heap
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            # Pop the first value if len is larger then k
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
