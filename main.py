import pygame
import random

from settings import *
from snake import Snake
from ai import ai_move
from level import generate_obstacles

# ========== INIT ==========
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Multiplayer Snake - FAST")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", FONT_SIZE)

# ========== SNAKES ==========
player = Snake(100, 100, GREEN, {
    "UP": pygame.K_w,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_a,
    "RIGHT": pygame.K_d
})

player2 = Snake(300, 300, BLUE, {
    "UP": pygame.K_UP,
    "DOWN": pygame.K_DOWN,
    "LEFT": pygame.K_LEFT,
    "RIGHT": pygame.K_RIGHT
})

ai_snake = Snake(500, 200, RED)

# ========== GAME DATA ==========
level = 1
obstacles = generate_obstacles(level)

def spawn_food():
    while True:
        pos = (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
        )
        if pos not in obstacles:
            return pos

food = spawn_food()

# ⏱️ TIME BASED SPEED
last_move_time = pygame.time.get_ticks()

# ========== MAIN LOOP ==========
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- INPUT ----
    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    player2.handle_input(keys)

    # ---- AI ----
    ai_move(ai_snake, food, obstacles)

    # ---- FAST MOVEMENT ----
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= SNAKE_DELAY:
        player.move()
        player2.move()
        ai_snake.move()
        last_move_time = current_time

    # ---- FOOD ----
    for snake in [player, player2, ai_snake]:
        if snake.body[0] == food:
            snake.grow = True
            food = spawn_food()
            level += 1
            obstacles = generate_obstacles(level)

    # ---- DRAW ----
    screen.fill(BLACK)

    for obs in obstacles:
        pygame.draw.rect(screen, GRAY, (*obs, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, WHITE, (*food, CELL_SIZE, CELL_SIZE))

    player.draw(screen)
    player2.draw(screen)
    ai_snake.draw(screen)

    hud = font.render(f"Level: {level}", True, WHITE)
    screen.blit(hud, (10, 10))

    pygame.display.flip()

pygame.quit()
