import pygame
from settings import CELL_SIZE

class Snake:
    def __init__(self, x, y, color, controls=None):
        self.body = [(x, y)]
        self.direction = (1, 0)
        self.color = color
        self.controls = controls
        self.grow = False

    def handle_input(self, keys):
        if not self.controls:
            return
        if keys[self.controls["UP"]]:
            self.direction = (0, -1)
        elif keys[self.controls["DOWN"]]:
            self.direction = (0, 1)
        elif keys[self.controls["LEFT"]]:
            self.direction = (-1, 0)
        elif keys[self.controls["RIGHT"]]:
            self.direction = (1, 0)

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = (x + dx, y + dy)

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                self.color,
                (*segment, CELL_SIZE, CELL_SIZE),
                border_radius=4
            )