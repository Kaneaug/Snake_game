import pygame
import random

# Initialize game engine
pygame.init()

# Set up window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake block size
block_size = 10

# Font for displaying score
font = pygame.font.Font(None, 30)

def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, [0,0])

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, black, [block[0], block[1], block_size, block_size])

def update_snake(snake_head, snake_list, direction):
    if direction == "right":
        snake_head[0] += block_size
    elif direction == "left":
        snake_head[0] -= block_size
    elif direction == "up":
        snake_head[1] -= block_size
    elif direction == "down":
        snake_head[1] += block_size

    snake_list.insert(0, list(snake_head))
    return snake_list[:-1]

def generate_food():
    food = [random.randint(0, (500/block_size)) * block_size,
            random.randint(0, (500/block_size)) * block_size]
    return food

def game_over(snake_head, snake_list):
    if snake_head[0] >= 500 or snake_head[0] < 0:
        return True
    elif snake_head[1] >= 500 or snake_head[1] < 0:
        return True
    for block in snake_list[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            return True
    return False

# Initialize game variables
direction = "right"
snake_list = [[100,100], [90,100], [80,100]]
snake_head = [70,100]
food = generate_food()
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

 # Snake colors
 # Fill background color
screen.fill(white)

# Draw snake
draw_snake(snake_list)

# Display score
display_score(score)

# Update screen
pygame.display.update()
  
