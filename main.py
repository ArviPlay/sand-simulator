import pygame, random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sand Simulator")

clock = pygame.time.Clock()
FPS = 60
SAND_COLOR = (255, 200, 100)

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

    is_pressed = pygame.mouse.get_pressed() # mouse button press detection
    if is_pressed[0] == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x = mouse_x // BLOCK_SIZE
        y = mouse_y // BLOCK_SIZE
        if x >= 0 and x < 200:
            if y >= 0 and y < 150:
                grid[y][x] = 1

    for y in range(149, -1, -1): # sand physics simulation
        for x in range(200):
            if y == 149: continue
            if grid[y][x] == 1:
                if grid[y+1][x] == 0:
                    grid[y+1][x] = 2
                    grid[y][x] = 0
                elif x == 0:
                    if grid[y+1][x+1] == 0:
                        grid[y+1][x+1] = 2
                        grid[y][x] = 0
                elif x == 199:
                    if grid[y+1][x-1] == 0:
                        grid[y+1][x-1] = 2
                        grid[y][x] = 0
                elif grid[y+1][x-1] == 0 and grid[y+1][x+1] == 0:
                    rnd_num = random.randint(0,1)
                    if rnd_num == 0:
                        grid[y+1][x-1] = 2
                        grid[y][x] = 0
                    else:
                        grid[y+1][x+1] = 2
                        grid[y][x] = 0
                elif grid[y+1][x-1] == 0:
                    grid[y+1][x-1] = 2
                    grid[y][x] = 0
                elif grid[y+1][x+1] == 0:
                    grid[y+1][x+1] = 2
                    grid[y][x] = 0
    screen.fill((0,0,0))
    for y in range(150): # rendering
        for x in range(200):
            if grid[y][x] == 1 or grid[y][x] == 2:
                screen_x = x * BLOCK_SIZE
                screen_y = y * BLOCK_SIZE
                pygame.draw.rect(screen, SAND_COLOR, (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
    for y in range(150):
        for x in range(200):
            if grid[y][x] == 2: grid[y][x] = 1
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()