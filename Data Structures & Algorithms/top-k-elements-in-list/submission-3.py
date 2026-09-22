from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        return sorted(list(d.keys()), key = lambda x: -d[x])[:k]
