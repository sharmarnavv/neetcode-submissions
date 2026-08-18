class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleetstk = []
        for pos, speed in cars:
            arrival_time = (target - pos)/speed
            if not fleetstk or arrival_time > fleetstk[-1]:
                fleetstk.append(arrival_time)
            else:
                continue
        return len(fleetstk)