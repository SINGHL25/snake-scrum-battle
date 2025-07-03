# game_logic.py
import random

BOARD_SIZE = 20

class SnakeGame:
    def __init__(self, num_players):
        self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.snakes = {}
        for i in range(num_players):
            self.snakes[f'P{i+1}'] = {
                'body': [(random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))],
                'direction': random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT']),
                'alive': True,
                'points': 0
            }

    def move(self, player_id):
        snake = self.snakes[player_id]
        if not snake['alive']: return
        head_x, head_y = snake['body'][0]
        dir = snake['direction']
        new_head = {
            'UP': (head_x, head_y - 1),
            'DOWN': (head_x, head_y + 1),
            'LEFT': (head_x - 1, head_y),
            'RIGHT': (head_x + 1, head_y)
        }[dir]

        # Collision check
        if not (0 <= new_head[0] < BOARD_SIZE and 0 <= new_head[1] < BOARD_SIZE):
            snake['alive'] = False
            return

        # Update position
        snake['body'].insert(0, new_head)
        snake['body'].pop()

    def update_direction(self, player_id, direction):
        self.snakes[player_id]['direction'] = direction

    def get_game_state(self):
        return self.snakes
