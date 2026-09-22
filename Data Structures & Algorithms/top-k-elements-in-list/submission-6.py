from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int) # numero:cuenta

        for n in nums:
            counter[n] += 1

        buckets = defaultdict(list)

        for n, frec in counter.items():
            buckets[frec].append(n)

        sol = []

        for thress in range(len(nums), 0, -1):
            n = buckets.get(thress)

            if n:
                sol.extend(n)
                if len(sol) >= k:
                    return sol[:k]