import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rainbow")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()