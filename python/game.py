import pygame
import string 
from variables import deadline, quiz_list, SCS, window, WHITE, BLUE, PASTEL_YELLOW, GOLD;
from variables import score, timer, turn

import variables as v


def run_game(level):
	from classes import Character, Text;
	from functions import check_input, clean_game, collision, create_buttons, hp_bar, potion_loop, projectile_loop, quiz_randomizer, update_score;
	from variables import bullets, buttons, inputs, objects, potions;
 
	v.score = 0
	quiz_randomizer(level)
 
	global question_text; question_text = Text([SCS[0]/3, SCS[1]/2], quiz_list[0][1])
	global turn_text; turn_text = Text([990, -64], f"TURN: {str(turn)}")
	global score_text; score_text = Text([990, -32], f"SCORE: {str(score)}")
	create_buttons(quiz_list[0][2], quiz_list[0][3], quiz_list[0][4], quiz_list[0][5])
	pressing = False

	global character; character = Character([SCS[0] / 2, SCS[1] / 2], [50, 50], 14)
	
	run = True
	frame = 0

	if level == "PRIMERO_MEDIO": 
		level_bg = "assets/background/1MEDIO.jpg"
		pygame.mixer.music.load("assets/OST/Every End.mp3")
		v.year = 1
	elif level == "SEGUNDO_MEDIO":
		level_bg = "assets/background/2MEDIO.jpg"
		pygame.mixer.music.load("assets/OST/Menace.mp3") 
		v.year = 2
	elif level == "TERCERO_MEDIO":
		level_bg = "assets/background/3MEDIO.jpg"
		pygame.mixer.music.load("assets/OST/ASDM ORG OST.mp3") 
		v.year = 3
	elif level == "CUARTO_MEDIO":
		level_bg = "assets/background/4MEDIO.jpg"
		pygame.mixer.music.load("assets/OST/SKRILLEX - KYOTO.mp3") 
		v.year = 4
	
	pygame.mixer.music.play(loops= -1)


	while run:
		window.blit(pygame.transform.scale(pygame.image.load(level_bg), SCS), (0, 0))
		timer.tick(60)
		frame += 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT: clean_game(); run = False
			elif event.type == pygame.KEYDOWN: check_input(event.key, True)
			elif event.type == pygame.KEYUP:	 check_input(event.key, False)

		for obj in objects: obj.update()

		for p in bullets:
			if collision(p, character) and character.inv <= 0:
				if p.type != "healer":
					character.hurt(p.dmg)
				else:
					character.heal(p.dmg)
				if p.destroyable: p.dissapear(); continue

			if not (deadline['left'] <= p.x <= deadline['right'] and deadline['top'] <= p.y <= deadline['bottom']):	p.dissapear()

		for p in potions:
			if collision(p, character) and inputs['c']:
				character.heal(p.heal)
				potions.remove(p); objects.remove(p)
		
		
		for b in buttons:
			if collision(b, character):
				if inputs['c'] and not pressing:
					pressing = True
					check = b.press()
					if check == False:
						character.hurt(3)
						character.inv = 0
						update_score(-200)
				elif not inputs['c']:
					b.imgname = "idle"
					b.img = pygame.image.load("assets/OBJ/buttons/idle.png")
			else:
				b.imgname = "idle"
				b.img = pygame.image.load("assets/OBJ/buttons/idle.png")
		pressing = inputs['c']
		
		potion_loop(frame)
		projectile_loop(frame, v.diff)
		if character.hp <= 0: game_over_screen("GAME OVER")

		hp_bar()
		pygame.display.update()


def game_over_screen(TITLE):
	from variables import FONT_20, FONT_40, FONT_100
	from screens import main_menu
	from functions import clean_game, draw_text, draw_initials_input
	from DB_functions import insert_player
	
	clean_game()

	if TITLE == "GAME OVER":
		background = "assets/background/GAME_OVER.jpg"
		COLOR = WHITE
	elif TITLE == "VICTORY":
		background = "assets/background/VICTORY.jpg"
		COLOR = PASTEL_YELLOW
	
	font = FONT_100
	medium_font = FONT_40
	small_font = FONT_20
	game_over = True

	
	initials_entered = False 

	character_set = list(string.ascii_uppercase) + list(string.digits)
	set_size = len(character_set) 
	max_initials = 6

	initials = ['A'] * max_initials
	initial_index = [0] * max_initials 
	cursor_position = 0


	while game_over:
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				exit()
			
			if event.type == pygame.KEYDOWN and not initials_entered:
					
				if event.key == pygame.K_RIGHT:
					cursor_position = (cursor_position + 1) % max_initials
					
				elif event.key == pygame.K_LEFT:
					cursor_position = (cursor_position - 1 + max_initials) % max_initials
					
				elif event.key in (pygame.K_UP, pygame.K_DOWN):
					direction = 1 if event.key == pygame.K_UP else -1
					current_index = initial_index[cursor_position]

					new_index = (current_index + direction + set_size) % set_size
						
					initial_index[cursor_position] = new_index
					initials[cursor_position] = character_set[new_index]

				elif event.key == pygame.K_RETURN:
					final_name = "".join(initials)
					if final_name != "AAAAAA":
						insert_player(final_name, v.score)
						
					initials_entered = True
					game_over = False 


		window.blit(pygame.transform.scale(pygame.image.load(background), SCS), (0, 0))
		
		draw_text(TITLE, font, BLUE, window, SCS[0] // 2, 100)
		draw_text(f"Puntuación: {str(v.score)}", medium_font, COLOR, window, SCS[0] // 2, 180)
		
		if not initials_entered:
			draw_text("INGRESA TUS INICIALES", medium_font, COLOR, window, SCS[0] // 2, 250)
			draw_text("(O dejalas así para saltar)", small_font, COLOR, window, SCS[0] // 2, 300)
				
			draw_initials_input(window, initials, cursor_position)
				
			draw_text("UP/DOWN: Cambiar | LEFT/RIGHT: Mover | ENTER: Confirmar", 
			small_font, COLOR, window, SCS[0] // 2, SCS[1] - 50)

				
		pygame.display.flip() 
		timer.tick(60)

	main_menu()