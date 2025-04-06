import pygame
import time
import random

pygame.init()


white = (255, 255, 255)
black = (20, 20, 20)
red = (200, 50, 10)
green = (10, 150, 50)
blue = (50, 153, 213)


display_width = 600
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_block = 15
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False
    
    x = display_width / 2
    y = display_height / 2
    x_change = 0
    y_change = 0
    direction = "STOP"
    
    snake_list = []
    length_of_snake = 1
    
    food_x = round(random.randrange(0, display_width - snake_block) / 15.0) * 15.0
    food_y = round(random.randrange(0, display_height - snake_block) / 15.0) * 15.0
    
    while not game_over:
        while game_close:
            display.fill(black)
            message("Game Over! Press C-Play Again or Q-Quit", red, display_width / 6, display_height / 3)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and direction != "RIGHT":
                    x_change = -snake_block
                    y_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_d and direction != "LEFT":
                    x_change = snake_block
                    y_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_w and direction != "DOWN":
                    y_change = -snake_block
                    x_change = 0
                    direction = "UP"
                elif event.key == pygame.K_s and direction != "UP":
                    y_change = snake_block
                    x_change = 0
                    direction = "DOWN"
        
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        display.fill(black)
        pygame.draw.circle(display, red, (int(food_x) + snake_block // 2, int(food_y) + snake_block // 2), snake_block // 2)
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        
        draw_snake(snake_block, snake_list)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 15.0) * 15.0
            food_y = round(random.randrange(0, display_height - snake_block) / 15.0) * 15.0
            length_of_snake += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

game_loop()
