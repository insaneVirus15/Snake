import pygame
import random
import os
from pygame import mixer

pygame.mixer.init()

#initialising pygame
pygame.init()

#creating window
screen_width = 300
screen_height = 400
game_window = pygame.display.set_mode((screen_width,screen_height))


#background image
bgimg = pygame.image.load(r"C:\Users\mpstate mining\Downloads\b.png")
pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption("Snake")
pygame.display.update()


#colors
white = (255,255,255)
red = (255,0,0)
green = (20,90,50)
blue = (0,0,255)
black = (0,0,0)



# game specific variables shifted ##########

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)
font_restart = pygame.font.SysFont(None,20)
font_score = pygame.font.SysFont(None,21)

def score_text(text,color,x,y):
    score_text = font_score.render(text, True, color)
    game_window.blit(score_text, [x, y])

def playagain(text,color,x,y):
    restart_text = font_restart.render(text,True,color)
    game_window.blit(restart_text,[x,y])

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color,snake_list,snake_size):
    #print(snake_list)
    for x,y in snake_list:
        #pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])
        pygame.draw.circle(game_window, color, [x, y], 9, 10)

def pause():
    #print("paused")
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False

                elif event.key == pygame.K_SPACE:
                    quit()




# snake list and snake len shifted ########

#game loop

def gameloop():

    snake_list = []
    snake_length = 1

    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 80
    snake_y = 150
    snake_size = 15
    fps = 60
    vel_x = 0
    vel_y = 0
    food_x = random.randint(0, screen_width - 20)
    food_y = random.randint(200, screen_height - 20)
    food_size = 20
    score = 0
    initial_velo = 0.9

    #check if highscore.txt file exist or not
    if (not os.path.exists("highscore.txt")):
        with open("highscore","w") as f:
            f.write("0")
    else:
        with open("highscore.txt","r") as f:
            highscore = f.read()


    while not exit_game:


        if game_over:

            #game_window.fill(white)
            img = pygame.image.load(r"C:\Users\mpstate mining\Downloads\b.png")
            pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
            game_window.blit(img, (0, 0))
            #game_window.blit(board, (0, 0))

            text_screen("Game Over! ", red,40 , 120)
            playagain("Press Enter To Play Again.",black,67,160)

            if score == 1000:
                score_text("YOUR SCORE: " + str(score), blue, 83, 240)
            elif score >= 10 and score <= 99:
                score_text("YOUR SCORE: 00" + str(score), blue, 83, 240)
            elif score >= 100 and score <= 999:
                score_text("YOUR SCORE: 0" + str(score), blue, 83, 240)
            else:
                score_text("YOUR SCORE: 000" + str(score), blue, 83 , 240)

            if int(highscore) == 1000:
                score_text("HIGHSCORE: " + str(highscore), blue, 85, 220)
            elif int(highscore) >= 10 and int(highscore) <= 99:
                score_text("HIGHSCORE: 00" + str(highscore), blue, 85, 220)
            elif int(highscore) >= 100 and int(highscore) <= 999:
                score_text("HIGHSCORE: 0" + str(highscore), blue, 85, 220)
            else:
                score_text("HIGHSCORE: 000" + str(highscore), blue, 85, 220)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #game_window.fill(white)
                        #text_screen("Paused", red, 40, 150)
                        pause()

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #snake_x = snake_x + 10
                        vel_x = initial_velo
                        vel_y = 0


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        #snake_x = snake_x - 10
                        vel_x = - initial_velo
                        vel_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #snake_y = snake_y - 10
                        vel_x = 0
                        vel_y = - initial_velo

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        #snake_y = snake_y + 10
                        vel_x = 0
                        vel_y = initial_velo

                if event.type == pygame.K_SPACE:
                    if event.key == pygame.K_SPACE:
                        pause()

                #speed control
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        initial_velo = 0.5

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        initial_velo = 0.6

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        initial_velo = 0.7

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_4:
                        initial_velo = 0.8

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_5:
                        initial_velo = 0.9

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_6:
                        initial_velo = 1.1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_7:
                        initial_velo = 1.2

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_8:
                        initial_velo = 1.3

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_9:
                        initial_velo = 1.4

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        #pygame.mixer.music.load(r'C:\Users\mpstate mining\Downloads\over.wav')
                        pygame.mixer.stop()




            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y

            if abs(snake_x - food_x) < 13 and abs(snake_y - food_y) < 13:

                pygame.mixer.music.load(r'C:\Users\mpstate mining\Downloads\eat.wav')
                pygame.mixer.music.play()

                score = score + 10
                #print(score)
                food_x = random.randint(0,screen_width-20)
                food_y = random.randint(100,screen_height-20)
                snake_length = snake_length + 40

                if score > int(highscore):
                    highscore = score
                    with open("highscore.txt", "w") as f:
                        f.write(str(highscore))

                #print(highscore)

            game_window.fill(white)
            game_window.blit(bgimg,(0,0))
            pygame.draw.rect(game_window, black, [0, 0, 300, 70])

            if score == 1000:
               text_screen("Score: " + str(score),white, 40, 20)
            elif score >= 10 and score <= 99:
                text_screen("Score: 00" + str(score),white, 40, 20)
            elif score >= 100 and score <= 999:
                text_screen("Score: 0" + str(score),white, 40, 20)
            else:
                text_screen("Score: 000" + str(score),white, 40, 20)

            #pygame.draw.rect(game_window,red,[food_x,food_y,food_size,food_size])
            pygame.draw.circle(game_window,red,[food_x,food_y],9,10)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                pygame.mixer.music.load(r'C:\Users\mpstate mining\Downloads\over.wav')
                pygame.mixer.music.play()
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 70 or snake_y > screen_height:
                pygame.mixer.music.load(r'C:\Users\mpstate mining\Downloads\over.wav')
                pygame.mixer.music.play()
                game_over = True
                #print("game over")



            #pygame.draw.rect(game_window,green,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(game_window,green,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()