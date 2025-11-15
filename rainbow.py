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
    
    colors = colors[1:] + [colors[0]]
    for i in range(len(colors)):
        pygame.draw.circle(screen, colors[i], (size_x // 2, size_y // 2),
        100 + i * 30, 30, draw_top_left=True, draw_top_right=True) 
    
    pygame.display.flip()
    clock.tick(4)


pygame.quit()