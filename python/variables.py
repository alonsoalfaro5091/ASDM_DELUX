import pygame

pygame.init()

SCS = (1280, 720)

window = pygame.display.set_mode(SCS)
pygame.display.set_caption("ASDM DELUXE")

timer = pygame.time.Clock()
FONT_PATH = 'assets/OBJ/fonts/aurora-24.ttf' 


try:
	FONT_100 = pygame.font.Font(FONT_PATH, 100)
	FONT_60 = pygame.font.Font(FONT_PATH, 60)
	FONT_40 = pygame.font.Font(FONT_PATH, 40)
	FONT_30 = pygame.font.Font(FONT_PATH, 28)
	FONT_20 = pygame.font.Font(FONT_PATH, 20)
except pygame.error as e:
	FONT_60 = pygame.font.SysFont(None, 60)
	FONT_40 = pygame.font.SysFont(None, 40)
	FONT_30 = pygame.font.SysFont(None, 30)
	FONT_20 = pygame.font.SysFont(None, 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = 	(255, 0, 0)
BLUE =	(35, 35, 255)
PASTEL_YELLOW =(255,238,140)
GOLD = (239,191,4)

inputs = {
	'up': False,
	'left': False,
	'down': False,
	'right': False,
	'z': False,
	'x': False,
	'c': False
}
deadline = {
	'top': -256,
	'left': -256,
	'bottom': SCS[1] + 256,
	'right': SCS[0] + 256
}
arena = {
	'top': 64,
	'left': 64,
	'bottom': SCS[1] - 64,
	'right': SCS[0] - 64
}
quiz_list = []

objects = []
bullets = []
buttons = []
enemies = []
potions = []

diff = 1
turn = 0
score = 0

year = 1