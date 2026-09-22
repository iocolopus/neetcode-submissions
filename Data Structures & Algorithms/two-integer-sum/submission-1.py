class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        dictionary = dict()

        for i_a, n in enumerate(nums):

            if dictionary.get(target - n) == None:
                dictionary[target - n] = i_a

            i_b = dictionary.get(n)

            if i_b != None and i_a != i_b:
                return [i_b, i_a]