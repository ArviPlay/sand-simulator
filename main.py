import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sand Simulator")

clock = pygame.time.Clock()
FPS = 60

grid = []
for y in range(150): # create a 2d grid
    row = []
    for x in range(200):
        row.append(0)
    grid.append(row)
BLOCK_SIZE = 4

running = True
while running:
    for event in pygame.event.get(): # events
        if event.type == pygame.QUIT:
            running = False
    
    for y in range(150): # rendering
        for x in range(200):
            if grid[y][x] == 1 or grid[y][x] == 2:
                screen_x = x * BLOCK_SIZE
                screen_y = y * BLOCK_SIZE
                pygame.draw.rect(screen, (255, 0, 0), (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()