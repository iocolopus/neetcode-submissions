from functools import reduce
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)

        p = [1] * l
        s = [1] * l

        for i in range(1, l):
            p[i] = p[i - 1] * nums[i - 1]

        for i in range (l - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]

        return [p[i] * s[i] for i in range(l)] 
        