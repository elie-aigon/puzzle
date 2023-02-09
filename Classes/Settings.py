import pygame, json

pygame.init()
# Game variables


# Colors
grey = (34,45,46)
white = (255, 255, 255)

# Font
font_win_mess = pygame.font.Font("Data/Font/upheavtt.ttf", 50)
font_block = pygame.font.Font("Data/Font/upheavtt.ttf", 39)
font_pixel = pygame.font.Font("Data/Font/upheavtt.ttf", 25)
font_title = pygame.font.Font("Data/Font/upheavtt.ttf", 75)
# Json
with open('Data/JSON/scores.json', 'r') as f:
    scores_dic = json.load(f)

# Clock
TIMER_UPDATE = pygame.USEREVENT
pygame.time.set_timer(TIMER_UPDATE, 1000)
