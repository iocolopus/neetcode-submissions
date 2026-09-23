class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        b_seq = set()

        for n in nums:
            if n-1 not in nums:
                b_seq.add(n)

        c_max = 0

        for b_n in b_seq:
            c = 1
            while b_n + c in nums:
                c += 1

            c_max = c if c_max < c else c_max

        return c_max
        