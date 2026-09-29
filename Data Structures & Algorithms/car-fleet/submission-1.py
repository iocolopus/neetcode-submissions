class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: -x[0])

        canon_tf = 0
        sol = 0

        for p, s in pos_speed:
            tf = (target - p) / s

            if tf > canon_tf:
                sol += 1
                canon_tf = tf

        return sol
            