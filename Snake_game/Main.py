import pygame
import random
pygame.init()
                        #init colors for the game
white = (255, 255, 255) 
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 102, 255)
                        #init height & weight of gui
dis_width = 600
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake game project")

clock = pygame.time.Clock() #Clock for game

#snake dimensions & speed
snake_blk = 10
snake_speed = 15

#fonts used in game
font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

#Score projector
def Your_score(score):
    value = score_font.render("your score:" + str(score), True, yellow)
    dis.blit(value, [0, 0])

#Building the snake
def our_snake(snake_blk, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_blk, snake_blk])

#Message display
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

#Main loop
def gameloop():
    gameover = False
    gamecls = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Lenght_of_snake = 1
                                                                            #Co-ordinates of food for snake 
    foodx = round(random.randrange(0, dis_width - snake_blk) / 10.0) * 10.0    
    foody = round(random.randrange(0, dis_height - snake_blk) / 10.0) * 10.0
                            #Gameplay loop
    while not gameover:
        while gamecls == True:
            dis.fill(blue)
            message("You lost press C-play again or Q-quit ", red)
            Your_score(Lenght_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameover = True
                            gamecls = False
                        if event.key == pygame.K_c:
                            gameloop()          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_blk
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_blk
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_blk
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_blk
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            gamecls = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_blk, snake_blk])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Lenght_of_snake:
            del snake_List[0]       
        for x in snake_List[:-1]:
            if x == snake_head:
                gamecls = True
        our_snake(snake_blk, snake_List) 
        Your_score(Lenght_of_snake-1)  #Score counter
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_blk)/10.0)*10.0
            foody = round(random.randrange(0, dis_height - snake_blk)/10.0)*10.0
            Lenght_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameloop()
