import pygame, math
from variables import inputs, window, arena, bullets, objects, potions;
from variables import window, WHITE;

class Object:
	def __init__(self, pos, size, img, speed=0, angle=0):
		self.x, self.y = pos
		self.width, self.height = size
		self.img = img

		self.speed = speed
		self.angle = angle

		objects.append(self)
	
	def draw(self): window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
  
	def update(self, draw=True, move=True):
		if move:
			self.x += math.cos(self.angle) * self.speed
			self.y += math.sin(self.angle) * self.speed
		if draw: self.draw()

	def center(self): return self.x + self.width / 2, self.y + self.height / 2

	def change_angle(self, target=None, angle=None):
		if target is not None:		self.angle = math.atan2(target[1] - self.y, target[0] - self.x)
		elif angle is not None: 	self.angle = math.radians(angle)
		else:											self.angle = 0


class Button(Object):
	def __init__(self, pos, size, id):
		super().__init__(pos, size, pygame.image.load("assets/OBJ/buttons/idle.png")) 
		self.imgname = "idle"
		self.id = id
		self.text = ""


	def draw(self):
		font_button = pygame.font.SysFont(None, 26)
		super().draw()
		
		if self.text:
			try: text_surface = font_button.render(self.text, True, WHITE) 
			except NameError:
				temp_font = pygame.font.SysFont(None, 20)
				text_surface = temp_font.render(self.text, True, WHITE)
			except Exception: return 

			if text_surface:
				text_rect = text_surface.get_rect(center=self.center())
				window.blit(text_surface, text_rect)

	def press(self):
		from variables import quiz_list, turn;
		from functions import change_turn;
		import game as g;
		self.imgname = "pressed"; self.img = pygame.image.load("assets/OBJ/buttons/pressed.png")
		if quiz_list[turn][6] == self.text:
			change_turn()
			return True
		else: return False


class Character(Object):
	def __init__(self, pos, size, speed=10, angle=0):
		super().__init__(pos, size, pygame.image.load("assets/character/right.png"), speed, angle)
		self.maxhp = self.hp = 10
		self.nohit = True

		self.inv = 0
		self.imgname = "right"
		
	def movement(self):
		dx, dy = inputs['right'] - inputs['left'], inputs['down']  - inputs['up']

		if dx < 0 and self.imgname == "right":	self.img = pygame.image.load("assets/character/left.png"); self.imgname = "left"
		if dx > 0 and self.imgname == "left": self.img = pygame.image.load("assets/character/right.png"); self.imgname = "right"

		if dx != 0 or dy != 0:
			self.angle = math.atan2(dy, dx)
			return True

		else: return False

	def update(self):
		canmove = self.movement()
		if self.inv > 0: self.inv -= 1

		if 9 > self.inv % 10 > 4: drawable = False
		else: drawable = True
		super().update(drawable, canmove)
		
		self.x = max(arena['left'], min(self.x, arena['right'] - self.width))
		self.y = max(arena['top'],	 min(self.y, arena['bottom'] - self.height))
		

	def hurt(self, damage):
		if damage > 0:
			self.hp -= damage
			self.inv = 75
			if self.nohit: self.nohit = False
			sfx = pygame.mixer.Sound("assets/SFX/hurt.mp3")
			sfx.play()
		else:
			self.heal(-damage)

	def heal(self, heal):
		from functions import update_score;
		if self.hp < self.maxhp:
			self.hp = self.maxhp if self.hp + heal >= self.maxhp else self.hp + heal
		else:
			update_score(heal * 200)
		sfx = pygame.mixer.Sound("assets/SFX/heal.mp3")
		sfx.play()
  

class Potion(Object):
	def __init__(self, pos, type):
		self.type = type
		speed = 0

		if type == "basic":
			size = [64, 64]
			img = pygame.image.load("assets/OBJ/potion.png")
			self.heal = 3
		if type == "super":
			size = [64, 64]
			img = pygame.image.load("assets/OBJ/superpotion.png")
			self.heal = 6

		super().__init__(pos, size, img, speed)
		potions.append(self)


class Projectile(Object):
	def __init__(self, pos, type, target=None, angle=None):
		self.delay = 30
		self.dmg = 1
		self.destroyable = True
		self.type = type

		if type == "basic01": 	img = pygame.image.load("assets/OBJ/attacks/bullet.png"); self.size = [16, 16]; speed = 12
		if type == "large01":		img = pygame.image.load("assets/OBJ/attacks/bullet.png"); self.size = [32, 32]; speed = 12; self.dmg = 2; self.destroyable = False
		if type == "linear01":	img = pygame.image.load("assets/OBJ/attacks/bone01.png"); self.size = [60, 20]; speed = 15; self.delay = 45
		if type == "linear02":	img = pygame.image.load("assets/OBJ/attacks/bone02.png"); self.size = [20, 60]; speed = 15; self.delay = 45
		if type == "multi":  		img = pygame.image.load("assets/OBJ/attacks/bullet.png"); self.size = [16, 16]; speed = 10
		if type == "healer":		img = pygame.image.load("assets/OBJ/attacks/healer.png"); self.size = [20, 20]; speed = 10; self.dmg = 2
		super().__init__(pos, self.size, img, speed)
		
		if target is not None:
			self.angle = math.atan2(target[1] - self.y, target[0] - self.x)
		else: self.angle = math.radians(angle)
		
		bullets.append(self)
	
	def dissapear(self): bullets.remove(self); objects.remove(self); del self
	
	def update(self):
		if self.delay > 0: self.delay -= 1; self.draw()
		else: super().update()


class Text(Object):
	def __init__(self, pos, text):
		from variables import FONT_20
		size = [400, 200]
		img = pygame.image.load("assets/OBJ/blank.png")
		self.text = text
		self.font = FONT_20
		super().__init__(pos, size, img)
  
	def draw(self):
		from variables import FONT_20
		font_button = FONT_20
		super().draw()
		
		if self.text:
			try: text_surface = font_button.render(self.text, True, WHITE) 
			except NameError:
				temp_font = pygame.font.SysFont(None, 20)
				text_surface = temp_font.render(self.text, True, WHITE)
			except Exception: return

			if text_surface:
				text_rect = text_surface.get_rect(center=self.center())
				window.blit(text_surface, text_rect)