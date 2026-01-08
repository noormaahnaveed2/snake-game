import random
from settings import WIDTH, HEIGHT, CELL_SIZE

def generate_obstacles(level):
    obstacles = set()
    for _ in range(level * 5):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        obstacles.add((x, y))
    return obstacles