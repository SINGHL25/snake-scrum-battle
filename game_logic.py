import random

BOARD_SIZE = 20

class Snake:
    def __init__(self, name):
        self.name = name
        self.body = [(random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.alive = True
        self.score = 0

    def move(self):
        if not self.alive:
            return
        head_x, head_y = self.body[0]
        dx, dy = {
            "UP": (0, -1),
            "DOWN": (0, 1),
            "LEFT": (-1, 0),
            "RIGHT": (1, 0)
        }[self.direction]
        new_head = (head_x + dx, head_y + dy)
        if 0 <= new_head[0] < BOARD_SIZE and 0 <= new_head[1] < BOARD_SIZE:
            self.body.insert(0, new_head)
            self.body.pop()
            self.score += 1
        else:
            self.alive = False

def get_winner(snakes):
    alive = [s for s in snakes if s.alive]
    if len(alive) == 1:
        return alive[0].name
    return None
