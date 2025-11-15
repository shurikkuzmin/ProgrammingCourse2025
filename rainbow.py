import pygame

pygame.init()

size_x = 800
size_y = 600

size = (size_x, size_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rainbow")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.circle(screen, "blue", (size_x // 2, size_y // 2),
        300) 
    pygame.display.flip()
    clock.tick(60)


pygame.quit()