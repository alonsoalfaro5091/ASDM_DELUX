import pygame, math, random
from variables import arena, buttons, inputs, SCS, WHITE, PASTEL_YELLOW, GOLD;
from classes import Button, Potion, Projectile;

import variables as v


def border_placement(section=None, margin=0):
	if section is None: section = random.randint(0, 3)
	if section == 0: x, y = random.randint(arena["left"] + margin, arena["right"] - margin), arena["top"] + margin
	if section == 1: x, y = arena["left"] + margin, random.randint(arena["top"] + margin, arena["bottom"] - margin)
	if section == 2: x, y = random.randint(arena["left"] + margin, arena["right"] - margin), arena["bottom"] - margin
	if section == 3: x, y = arena["right"] - margin, random.randint(arena["top"] + margin, arena["bottom"] - margin)
	return x, y


def check_input(key, value):
	if key in (pygame.K_UP, pygame.K_w):		inputs['up'] = value
	if key in (pygame.K_LEFT, pygame.K_a):		inputs['left'] = value
	if key in (pygame.K_DOWN, pygame.K_s):		inputs['down'] = value
	if key in (pygame.K_RIGHT, pygame.K_d):		inputs['right'] = value
	if key == pygame.K_z:											inputs['z'] = value
	if key == pygame.K_x:											inputs['x'] = value
	if key == pygame.K_c:											inputs['c'] = value


def collision(origin, target):
	x1, y1, = origin.center()
	x2, y2, = target.center()
	w1, h1 = origin.width / 2, origin.height / 2
	w2, h2 = target.width / 2, target.height / 2
	if x1 + w1 > x2 - w2 and x1 - w1 < x2 + w2:
		return y1 + h1 > y2 - h2 and y1 - h1 < y2 + h2
	else: return False


def clean_game():
	for i in v.inputs: inputs[i] = False
	pygame.mixer.music.stop()
	v.bullets.clear(); v.buttons.clear()
	v.potions.clear(); v.objects.clear()
	v.quiz_list.clear(); v.turn = 0


def change_turn():
	from game import character, question_text, turn_text, game_over_screen;
	from variables import quiz_list
	v.turn += 1
	if v.turn % 10 == 0: v.diff += 1
	update_score(1000)

	if v.turn == 30:
		update_score(4000)
		if character.nohit: update_score(10000)
		game_over_screen("VICTORY")

	alts = [2, 3, 4, 5]
	random.shuffle(alts)
 
	question_text.text =	quiz_list[v.turn][1]
	buttons[0].text = 		quiz_list[v.turn][alts[0]]
	buttons[1].text = 		quiz_list[v.turn][alts[1]]
	buttons[2].text = 		quiz_list[v.turn][alts[2]]
	buttons[3].text = 		quiz_list[v.turn][alts[3]]

	turn_text.text =	f"TURN: {str(v.turn)}"


def spawn_button(obj, idx="add"):
	if idx == "add": buttons.append(obj)
	else: buttons[idx] = obj

def create_buttons(text01, text02, text03, text04):
	button_size = [245, 94]
	top, left = 100, 100
	bottom, right = SCS[1] - 100 - 94, SCS[0] - 100 - 245
	
	spawn_button(Button([left , top], button_size, 1))
	spawn_button(Button([right, top], button_size, 2))
	spawn_button(Button([left , bottom], button_size, 3))
	spawn_button(Button([right, bottom], button_size, 4))
	
	buttons[0].text = text01
	buttons[1].text = text02
	buttons[2].text = text03
	buttons[3].text = text04


def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, False, color)
	textrect = textobj.get_rect()
	textrect.center = (x, y)
	surface.blit(textobj, textrect)

def draw_text_centered(text, font, color, surface, rect):
	textobj = font.render(text, False, color)
	textrect = textobj.get_rect(center=rect.center)
	surface.blit(textobj, textrect)

def draw_initials_input(surface, initials, cursor_pos):
	max_initials = 6
	font = pygame.font.SysFont(None, 60) 
	total_width = max_initials * 60
	start_x = (SCS[0] - total_width) // 2 + 30
	y = SCS[1] // 2
			
	for i in range(max_initials):
		char = initials[i]
		x = start_x + (i * 60)

		color = GOLD if i == cursor_pos else PASTEL_YELLOW
		char_surface = font.render(char, True, color)
					
		surface.blit(char_surface, (x, y))
					
		if i == cursor_pos:
			pygame.draw.rect(surface, (255, 0, 0), (x, y + 60, 50, 5), 0)


def hp_bar():
	from game import character;
	from variables import window;
	if character.hp <= 0: return
	pos = (40, 10)
	size = (300, 20)
	pygame.draw.rect(window, (60, 60, 60), (*pos, *size))
	hp = character.hp / character.maxhp
	bg_fill = int(size[0] * hp)

	pygame.draw.rect(window, (255, 0, 0), (pos[0], pos[1], bg_fill, size[1]))
	pygame.draw.rect(window, WHITE, (*pos, *size), 2)

	font = pygame.font.SysFont(None, 28)
	text = font.render(f"HP: {character.hp}/{character.maxhp}", True, WHITE)
	window.blit(text, (pos[0] + 10, pos[1] - 2))


def spawn_projectiles(origin, count=3, spread=30, type="multi", extra=None, target=None, angle=None):
	from game import character
	if target is None and angle is None:
		target = character.center()
	if target is not None:
		main_angle = math.degrees(math.atan2(target[1] - origin[1], target[0] - origin[0]))
	else: main_angle = angle

	spread_angle = spread

	if count > 1:
		step = spread_angle / (count - 1)
		start_angle = main_angle - spread_angle / 2
	else:
		step = 0
		start_angle = main_angle
	
	if extra == 1:
		heal_bullet = random.randint(1, count - 1)

	projectiles = []
	for i in range(count):
		projectile_angle = start_angle + i * step
		if extra == 1 and i == heal_bullet:
			projectiles.append(Projectile(origin, "healer", angle=projectile_angle))
		else:
			projectiles.append(Projectile(origin, type, angle=projectile_angle))

	return projectiles


def potion_loop(frame):
	if frame % 960 == 300:
		pos = [random.randint(arena['left'] + 64, arena['right'] - 64), random.randint(arena['top'] + 64, arena['bottom'] - 64)]
		Potion(pos, "super" if random.randint(0, 3) == 0 else "basic")


def projectile_loop(frame, diff):
	from game import character;

	if frame % 90 == 25:
		x, y = border_placement()
		Projectile([x, y], "basic01", target=[SCS[0] / 2, SCS[1] / 2])

	if frame % 120 == 50 and diff != 2:
		x, y = border_placement()
		Projectile([x, y], "basic01", target=character.center())

	if frame % 140 == 47 and diff == 1:
		x, y = border_placement()
		Projectile([x, y], "basic01", target=[random.randint(arena["left"], arena["right"]), random.randint(arena["top"], arena["bottom"])])
	
	if frame % 70 == 0:
		section = random.randint(0, 3)
		if section == 0:
			x, y = border_placement(0)
			Projectile([x, y], "linear01", angle=90)
		if section == 1:
			x, y = border_placement(1)
			Projectile([x, y], "linear02", angle=0)
		if section == 2:
			x, y = border_placement(2)
			Projectile([x, y], "linear01", angle=-90)
		if section == 3:
			x, y = border_placement(3)
			Projectile([x, y], "linear02", angle=180)
	
	if frame % 240 == 90 and diff >= 2:
		x, y = border_placement()
		rng = random.randint(3, 5)
		heal = random.randint(0, 2)
		spawn_projectiles([x, y], count=rng, spread=rng*10, target=character.center(), extra=heal)
	
	if frame % 100 == 40 and diff >= 2:
		x, y = border_placement()
		Projectile([x, y], "large01", target=character.center())
	
	if frame % 320 == 160 and diff == 3:
		
		x, y = border_placement()
			
		p1 = Projectile([x, y], "basic01", target=[random.randint(arena["left"], arena["right"]), random.randint(arena["top"], arena["bottom"])])
		p2 = Projectile([x, y], "basic01", target=[random.randint(arena["left"], arena["right"]), random.randint(arena["top"], arena["bottom"])])
		p3 = Projectile([x, y], "basic01", target=[random.randint(arena["left"], arena["right"]), random.randint(arena["top"], arena["bottom"])])

		p2.delay = 45; p3.delay = 60



def update_score(points):
	from game import score_text;
	from variables import year;
	if points % 1000 == 0:
		if year == 1: multiplier = 1
		if year == 2: multiplier = 1.5
		if year == 3: multiplier = 2
		if year == 4: multiplier = 2.5
	else:
		multiplier = 1

	v.score += math.floor(points * multiplier)
	if v.score < 0: v.score = 0
	score_text.text = f"SCORE: {str(v.score)}"


def obtain_question(table_name, id_question):
	from DB_functions import obtain_data
	unique_answer = obtain_data(table_name, id_question)

	id = unique_answer[0]
	answer = unique_answer[1]
	alt01, alt02, alt03, alt04 = unique_answer[2:6]
	correct = unique_answer[6]
	
	return id, answer, alt01, alt02, alt03, alt04, correct
	

def quiz_randomizer(level):
	from variables import quiz_list; import random;

	id_level01 = list(range(1, 11))
	id_level02 = list(range(11, 21))
	id_level03 = list(range(21, 31))
	random.shuffle(id_level01); random.shuffle(id_level02); random.shuffle(id_level03)

	for id in range(30):
		if 0 <= id <= 9: cur_id = id_level01[id]
		if 10 <= id <= 19: cur_id = id_level02[id - 10]
		if 20 <= id <= 29: cur_id = id_level03[id - 20]

		quiz_list.append(obtain_question(level, cur_id))