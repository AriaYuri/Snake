import pygame
import time
import random

pygame.init()

yellow = (255, 255, 95)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 200)

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont('Times', 25)
score_font = pygame.font.SysFont('Times', 35)

def Your_score(score):
    value = score_font.render('Your score: ' + str(score), True, yellow)
    window.blit(value, [0, 0])

def player_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])

def GameWork():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            window.fill(blue)
            message('You lose! Press C to play again or Q to quit.', red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        GameWork()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        player_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

GameWork()