from collections import Counter, defaultdict        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        d = defaultdict(list)

        for i, s in enumerate(strs):

            count = [0] * 27

            for char in s:
                count[ord(char) - ord("a")] += 1

            d[tuple(count)].append(s)

        return list(d.values())

        
                