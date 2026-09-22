from collections import Counter, defaultdict        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_table = [[0] * 27 for _ in strs]

        d = defaultdict(list)

        for i, s in enumerate(strs):
            for char in s:
                hash_table[i][ord(char) - ord("a")] += 1

            d[tuple(hash_table[i])].append(s)

        return list(d.values())

                