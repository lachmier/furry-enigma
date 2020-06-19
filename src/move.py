import random

# 1: right, 2:
#       \|/
#       -|-
#       /|\

DIRECTION = {
    1: "Straight",
    2: "UpRight",
    3: "Right",
    4: "DownRight",
    5: "Down",
    6: "DownLeft",
    7: "Left",
    8: "UpLeft",
}


class Movement:
    def __init__(self, DIRECTION):
        self.direction = DIRECTION[random.randint(1, 8)]

    @property
    def move(self):
        return self.direction  # DIRECTION[random.randint(1, 8)]

    @move.setter
    def move(self, direction):
        self.direction = DIRECTION[direction]

    @property
    def dice(self):
        return random.randint(1, 8)


# test
movement = Movement(DIRECTION)
print(movement.move)
for i in range(10):
    movement.move = movement.dice
    print(movement.move)


# for i in range(10):
#     print(movement.move)
