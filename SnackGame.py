import pygame
import sys
import random

check_errors = pygame.init()
frame_size_x = 720
frame_size_y = 480
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

#fps added
fps_controller = pygame.time.Clock()

direction = 'RIGHT'
change_to = direction

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#snake
snake_pos = [100,50]
snake_body = [[100,50],[90,50],[80,50]]

apple_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
apple_spawn = True

score=0

while True:
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    game_window.fill(black)
    print(change_to)
    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
        apple_spawn = False
        score+=1
    else:
        snake_body.pop()

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
   
    if not apple_spawn:
        apple_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]

    apple_spawn = True
    pygame.draw.rect(game_window, red, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) 

    # Score Display
    score_font = pygame.font.SysFont('Arial', 20)
    score_surface = score_font.render( str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (360, 15)
    game_window.blit(score_surface, score_rect)

    pygame.display.update()
    fps_controller.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
               pygame.event.post(pygame.event.Event(pygame.QUIT))