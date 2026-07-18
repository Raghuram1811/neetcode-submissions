class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet = deque()

        cars = sorted(zip(position, speed), reverse = True)

        for pos, sp in cars:
            time = (target - pos)/sp
            fleet.append(time)

            if len(fleet)>=2 and fleet[-2]>=fleet[-1]:
                fleet.pop()
        return len(fleet)
