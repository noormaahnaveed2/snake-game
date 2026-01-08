import random

def ai_move(snake, food, obstacles):
    head_x, head_y = snake.body[0]
    fx, fy = food

    options = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    options.sort(
        key=lambda d: abs(head_x + d[0] - fx) + abs(head_y + d[1] - fy)
    )

    for dx, dy in options:
        new_pos = (head_x + dx, head_y + dy)
        if new_pos not in snake.body and new_pos not in obstacles:
            snake.direction = (dx, dy)
            return

    snake.direction = random.choice(options)