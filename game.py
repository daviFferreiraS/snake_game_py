import pygame
import time
import random

black = (0, 0, 0)
red = (255, 0, 0)
white = (255,255,255)
green = (0,255,0)
dis_width = 800
dis_height = 600
snake_block = 10
snake_speed = 20

pygame.init()

pygame.display.set_caption('Meu primeiro jogo dentro da aula de POO')
dis = pygame.display.set_mode((dis_width, dis_height))
bg = pygame.image.load("grass.jpg")

font_style = pygame.font.SysFont(None, 50)

def display_img():
    dis.blit(bg, (0,0))


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    

def message(msg, color):
    mensage = font_style.render(msg, True, color)
    dis.blit(mensage, [dis_width/6, dis_height/3])

clock = pygame.time.Clock()

def game_loop():
    # Movement control flags
    is_up = False
    is_down = False
    is_left = False
    is_right = False
    pygame.image.load("grass.jpg")
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    game_over = False
    game_close = False
    snake_list = []
    len_snake = 1

    foodx= round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        #establishing indeed the game loop, treating the "play again" scenario
        while game_close == True:
            dis.fill(white)
            message("Perdeu Playboy, (Q)uit / (P)lay Again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_p:
                        game_loop()
        #snake movements
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                game_over = True
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_UP and is_down == False):
                    y1_change = -snake_block
                    x1_change = 0
                    is_up = True
                    is_right = False
                    is_left = False
                elif(event.key == pygame.K_DOWN and is_up == False):
                    y1_change = snake_block
                    x1_change = 0
                    is_down = True
                    is_right = False
                    is_left = False
                elif(event.key == pygame.K_LEFT and is_right == False):
                    x1_change = -snake_block
                    y1_change = 0
                    is_left = True
                    is_up = False
                    is_down = False
                elif(event.key == pygame.K_RIGHT and is_left == False):
                    x1_change = snake_block
                    y1_change = 0
                    is_right = True
                    is_up = False
                    is_down = False

        #treating the conditions of the game to end
        if(x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0):
            game_close = True

        # adding the coordinates to compute in fact the movement    
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        #drawing the food
        pygame.draw.rect(dis, red, [foodx,foody,snake_block,snake_block])


        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if(len(snake_list) > len_snake):
            del snake_list[0]

      #  print(snake_list[:-1], snake_head)
        for x in snake_list[1:-1]:
            if x == snake_head:
                print("teste")
                game_close = True

        draw_snake(snake_block, snake_list)

        #display_img()
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx= round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            len_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

game_loop()
