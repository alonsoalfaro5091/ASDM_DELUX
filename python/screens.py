import pygame, sys
from DB_functions import show_player
from variables import SCS, WHITE, BLACK, GOLD, FONT_20, FONT_30, FONT_40, FONT_60, FONT_100;
from functions import draw_text, draw_text_centered;

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('BASE GAME')
screen = pygame.display.set_mode((1280, 700), 0, 32)
font_20 = FONT_20
FONT_30 = FONT_30
FONT_40 = FONT_40
FONT_60 = FONT_60
FONT_100 = FONT_100
bg_menu = pygame.image.load('assets/background/main_menu.jpg')
bg_niveles = pygame.image.load('assets/background/level_selection.jpg')
bg_ranking = pygame.image.load('assets/background/ranking.jpg')
 
click = False

def draw_data(screen, names, scores, start_y, row_font, color_white, color_score):

    row_height = 50
    x_pos_rank = 320
    x_pos_name = 640
    x_pos_score = 960
    

    draw_text('N°', row_font, color_white, screen, x_pos_rank, 100 ) 
    draw_text('NOMBRE', row_font, color_white, screen, x_pos_name, 100  )
    draw_text('PUNTUACIÓN', row_font, color_white, screen, x_pos_score, 100 )
    
    for index, (name, score) in enumerate(zip(names, scores)):
        if index >= 10:
            break
            
        y_pos = start_y + index * row_height

        draw_text(str(index + 1), row_font, color_white, screen, x_pos_rank, y_pos)

        draw_text(name, row_font, color_white, screen, x_pos_name, y_pos)
        
        draw_text(str(score), row_font, color_score, screen, x_pos_score, y_pos) 


def ranking():
    pygame.mouse.set_visible(True)
    click = False
    running = True

    names, scores = show_player()
      
    while running:

        screen.blit(bg_ranking, (0, 0))
        

        draw_data(screen, names, scores, start_y=150, row_font=FONT_30, color_white=WHITE, color_score=GOLD)
        

        button_volver = pygame.Rect(540, 600, 200, 60)
        pygame.draw.rect(screen, (0, 255, 255), button_volver)
        draw_text_centered('Volver', FONT_30, BLACK, screen, button_volver)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1: click = True
        
        mx, my = pygame.mouse.get_pos()
        if button_volver.collidepoint((mx, my)):
            if click: running = False
        
        click = False
        
        pygame.display.update()
        mainClock.tick(60)


def level_selection():
	click = False
	running = True
	while running:
		screen.blit(bg_niveles, (0, 0))
		draw_text('NIVELES', FONT_40, WHITE, screen, SCS[0]/2, 100)
	
		button_volver = pygame.Rect(540, 600, 200, 60)
		pygame.draw.rect(screen, (0, 255, 255), button_volver)
		draw_text_centered('Volver', FONT_30, BLACK, screen, button_volver)
	
		button_1_MEDIO = pygame.Rect(490, 200, 300, 60)
		pygame.draw.rect(screen, (0, 255, 255), button_1_MEDIO)
		draw_text_centered('Primero Medio', FONT_30, BLACK, screen, button_1_MEDIO)
	
		button_2_MEDIO = pygame.Rect(490, 280, 300, 60)
		pygame.draw.rect(screen, (0, 255, 255), button_2_MEDIO)
		draw_text_centered('Segundo Medio', FONT_30, BLACK, screen, button_2_MEDIO)
	
		button_3_MEDIO = pygame.Rect(490, 360, 300, 60)
		pygame.draw.rect(screen, (0, 255, 255), button_3_MEDIO)
		draw_text_centered('Tercero Medio', FONT_30, BLACK, screen, button_3_MEDIO)
	
		button_4_MEDIO = pygame.Rect(490, 440, 300, 60)
		pygame.draw.rect(screen, (0, 255, 255), button_4_MEDIO)
		draw_text_centered('Cuarto medio', FONT_30, BLACK, screen, button_4_MEDIO)
	
		for event in pygame.event.get():
			if event.type == QUIT: pygame.quit(); sys.exit()
			if event.type == KEYDOWN and event.key == K_ESCAPE: running = False
			if event.type == MOUSEBUTTONDOWN and event.button == 1: click = True
	
		mx, my = pygame.mouse.get_pos()
	
		if click == True:
			from game import run_game

			if button_volver.collidepoint((mx, my)): running = False
	
			if button_1_MEDIO.collidepoint((mx, my)): run_game("PRIMERO_MEDIO")
			if button_2_MEDIO.collidepoint((mx, my)): run_game("SEGUNDO_MEDIO")
			if button_3_MEDIO.collidepoint((mx, my)): run_game("TERCERO_MEDIO")
			if button_4_MEDIO.collidepoint((mx, my)): run_game("CUARTO_MEDIO")
	
		pygame.display.update()
		mainClock.tick(60)
 
def main_menu():
	pygame.mouse.set_visible(True)
	pygame.mixer.music.load("assets/OST/Dark Tides.mp3") 
	pygame.mixer.music.play(loops= -1)

	while True:
		global click
		screen.blit(bg_menu, (0, 0))
		draw_text('ASDM DELUXE', FONT_60, GOLD, screen, SCS[0]/2, 100)
		draw_text('MENÚ PRINCIPAL', FONT_40, WHITE, screen, SCS[0]/2, 200)
		
		click = False
		for event in pygame.event.get():
			if event.type == QUIT: pygame.quit(); sys.exit()
			if event.type == KEYDOWN and event.key == K_ESCAPE: pygame.quit(); sys.exit()
			if event.type == MOUSEBUTTONDOWN and event.button == 1: click = True

		mx, my = pygame.mouse.get_pos()

		button_ranking = pygame.Rect(540, 350, 200, 60)
		button_niveles = pygame.Rect(540, 450, 200, 60)
		button_salir = pygame.Rect(540, 550, 200, 60)

		if button_ranking.collidepoint((mx, my)) and click: ranking(); click = False
		if button_niveles.collidepoint((mx, my)) and click: level_selection(); click = False
		if button_salir.collidepoint((mx, my)) and click: pygame.quit(); sys.exit(); click = False

		pygame.draw.rect(screen, (0, 255, 255), button_ranking)
		pygame.draw.rect(screen, (0, 255, 255), button_niveles)
		pygame.draw.rect(screen, (255, 0, 0), button_salir)

		draw_text_centered('Ranking', FONT_30, BLACK, screen, button_ranking)
		draw_text_centered('Niveles', FONT_30, BLACK, screen, button_niveles)
		draw_text_centered('Salir', FONT_30, BLACK, screen, button_salir)

		pygame.display.update()
		mainClock.tick(60)

 
def options():
	pygame.mouse.set_visible(True)
	running = True
	while running:
		screen.fill((0,0,0))

		draw_text('options', FONT_30, WHITE, screen, 20, 20)
		for event in pygame.event.get():
			if event.type == QUIT: pygame.quit(); sys.exit()
			if event.type == KEYDOWN and event.key == K_ESCAPE: running = False
		
		pygame.display.update()
		mainClock.tick(60)
 
main_menu()