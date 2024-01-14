class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pos_to_speed = [(p, sp) for p, sp in zip(position, speed)]
        pos_to_speed = sorted(pos_to_speed, key=lambda x: x[0], reverse=True)
        print(pos_to_speed)

        count = 1
        if len(position) == 1:
            return count

        t_ride = (target - pos_to_speed[0][0]) / pos_to_speed[0][1]

        for i in range(1, len(pos_to_speed)):
            t_curr = (target - pos_to_speed[i][0]) / pos_to_speed[i][1]
            if t_curr <= t_ride:
                pass
            else:
                count += 1
                t_ride = t_curr

        return count

sol = Solution()
# target = 12
# position = [10, 8, 0, 5, 3]
# speed = [2, 4, 1, 1, 3]
# target = 100
# position = [0,2,4]
# speed = [4,2,1]
# target = 10
# position = [3]
# speed = [3]
# target = 10
# position = [6,8]
# speed = [3,2]
# target = 13
# position = [10,2,5,7,4,6,11]
# speed = [7,5,10,5,9,4,1]
# target = 27
# position = [19,25,16,11,23,9,18,0,10,17,3,14,12,20,5]
# speed = [7,9,6,3,3,5,1,8,3,6,10,4,6,2,6]
# target = 31
# position = [5,26,18,25,29,21,22,12,19,6]
# speed = [7,6,6,4,3,4,9,7,6,4]

print(sol.carFleet(target, position, speed))