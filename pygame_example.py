#!/usr/bin/env python3
"""Minimal pygame example.

Controls:
- Arrow keys: move the red circle
- Esc or window close: quit

Run: python3 pygame_example.py
Requires: pygame (see requirements.txt)
"""
import sys
import pygame


def main() -> None:
    pygame.init()
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Minimal Pygame Example")
    clock = pygame.time.Clock()

    x, y = size[0] // 2, size[1] // 2
    speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        # keep inside window
        x = max(0, min(size[0], x))
        y = max(0, min(size[1], y))

        screen.fill((30, 30, 30))
        pygame.draw.circle(screen, (200, 50, 50), (x, y), 20)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # If something unexpected happens, ensure pygame quits then re-raise
        try:
            pygame.quit()
        except Exception:
            pass
        raise
