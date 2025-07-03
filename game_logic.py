import random

BOARD_SIZE = 10

class Snake:
    def __init__(self, name, emoji):
        self.name = name
        self.emoji = emoji
        self.body = [(random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.alive = True
        self.score = 0

    def move(self, board):
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

        # Check boundaries and collisions
        if not (0 <= new_head[0] < BOARD_SIZE and 0 <= new_head[1] < BOARD_SIZE):
            self.alive = False
            return
        if board[new_head[1]][new_head[0]] != "":
            self.alive = False
            return

        # Move snake
        self.body.insert(0, new_head)
        self.body.pop()
        self.score += 1

    def update_direction(self):
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

def create_board(snakes):
    board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for snake in snakes:
        if snake.alive:
            for x, y in snake.body:
                board[y][x] = snake.emoji
    return board

def get_winner(snakes):
    alive_snakes = [s for s in snakes if s.alive]
    if len(alive_snakes) == 1:
        return alive_snakes[0]
    return None
