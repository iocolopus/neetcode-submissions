class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        canon_tf = 0
        sol = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            tf = (target - p) / s
            if tf > canon_tf:
                sol += 1
                canon_tf = tf

        return sol