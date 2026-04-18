# Top K Frequent (Streaming)

import heapq
from collections import defaultdict

class TopKFrequentStream:
    def __init__(self, k):
        self.k = k
        self.freq = defaultdict(int)   # HashMap: num -> frequency
        self.heap = []                 # Min Heap: (frequency, num)

    def add(self, num):
        # Step 1: Update frequency
        self.freq[num] += 1
        freq = self.freq[num]
        
        # Step 2: Push updated frequency into heap
        heapq.heappush(self.heap, (freq, num))

        # Step 3: Maintain heap size <= k
        if len(self.heap) > self.k:
             heapq.heappop(self.heap)

    def get_top_k(self):
        # Remove outdated entries (IMPORTANT)
        valid = []
        while self.heap:
            freq, num = heapq.heappop(self.heap)
            # Only keep latest valid frequency
            if self.freq[num] == freq:
                valid.append((freq, num))

        # Rebuild heap (since we popped everything)
        for item in valid:
            heapq.heappush(self.heap, item)

        # Return sorted result (highest frequency first)
        return [num for freq, num in sorted(valid, reverse=True)]

stream = TopKFrequentStream(k=2)

data = [1, 2, 1, 3, 2, 1]

for num in data:
    stream.add(num)

print(stream.get_top_k())