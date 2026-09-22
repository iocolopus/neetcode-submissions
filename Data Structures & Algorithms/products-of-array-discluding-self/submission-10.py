from functools import reduce
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n_zeros = sum([n == 0 for n in nums])

        sol = [0] * len(nums)


        if n_zeros == 1:
            idx = nums.index(0)

            sol[idx] = reduce(
                lambda x, y: x*y,
                [n if n != 0 else 1 for n in nums]
            )
        elif n_zeros == 0:
            prod = reduce(lambda x, y: x*y, nums)
            sol = [prod // n for n in nums]

        return sol

        


        