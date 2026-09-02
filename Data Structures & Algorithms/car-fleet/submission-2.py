class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stk = []
        for p, v in cars:
            if not stk or (target - p)/v > stk[-1]:
                stk.append((target-p)/v)
        return len(stk)
