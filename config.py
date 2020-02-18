import pygame
import random
import math
import time

screen=pygame.display.set_mode((800,630))
pygame.display.set_caption("River Crossing")

icon=pygame.image.load("icon.png")

playerImg=pygame.image.load("player.png")
fixed_obstacle1Img=pygame.image.load("fixed_obstacle1.png")
shipImg=pygame.image.load("ship.png")

player_status = 1
player1_score = 0
player2_score = 0
player1_time = 0
player2_time = 0
check1=0
check2=0
check3=0
check4=0

#font = pygame.font.Font("freesansbold.ttf",32)
font_used = "freesansbold.ttf"
start_text="PRESS ANY KEY"
start_time=time.time()

class Player:
	def __init__(self):
		self.X_cood = 400
		self.Y_cood = 600
		self.velocity = 0.3
		self.score=0
		return

	def move(self, pressed_key):
		global player_status
		global check1
		global check2
		global check3
		global check4

		if self.X_cood < self.velocity:
			self.X_cood = self.velocity
		if self.X_cood >= 768:
			self.X_cood = 768

		if self.Y_cood < self.velocity:
			self.Y_cood = self.velocity
		if self.Y_cood >= 600:
			self.Y_cood = 600		
		
		if pressed_key[pygame.K_LEFT] == True:
			self.X_cood -= self.velocity

		elif pressed_key[pygame.K_RIGHT] == True:
			self.X_cood += self.velocity

		elif pressed_key[pygame.K_UP] == True:
			self.Y_cood -= self.velocity

		elif pressed_key[pygame.K_DOWN] == True:
			self.Y_cood += self.velocity

		if player_status%2 == 1:
			if self.Y_cood<600 and check1 == 0:
				check1 = 1
				self.score += 5
			elif self.Y_cood<500 and check1 == 1:
				check1 = 2
				self.score += 5
			elif self.Y_cood<400 and check1 == 2:
				check1 = 3
				self.score += 5
			elif self.Y_cood<300 and check1 == 3:
				check1 = 4
				self.score += 5
			elif self.Y_cood<200 and check1 == 4:
				check1 = 5
				self.score += 5
			elif self.Y_cood<100 and check1 == 5:
				check1 = 6
				self.score += 5	

			if self.Y_cood<530 and check3 == 0:
				check3 = 1
				self.score += 10
			elif self.Y_cood<430 and check3 == 1:
				check3 = 2
				self.score += 10
			elif self.Y_cood<330 and check3 == 2:
				check3 = 3
				self.score += 10
			elif self.Y_cood<230 and check3 == 3:
				check3 = 4
				self.score += 10
			elif self.Y_cood<130 and check3 == 4:
				check3 = 5
				self.score += 10
			elif self.Y_cood<30 and check3 == 5:
				check3 = 6
				self.score += 10

		elif player_status%2 == 0:
			if self.Y_cood>30 and check2 == 0:
				check2 = 1
				self.score += 5
			elif self.Y_cood>130 and check2 == 1:
				check2 = 2
				self.score += 5
			elif self.Y_cood>230 and check2 == 2:
				check2 = 3
				self.score += 5
			elif self.Y_cood>330 and check2 == 3:
				check2 = 4
				self.score += 5
			elif self.Y_cood>430 and check2 == 4:
				check2 = 5
				self.score += 5
			elif self.Y_cood>530 and check2 == 5:
				check2 = 6
				self.score += 5	

			if self.Y_cood>100 and check4 == 0:
				check4 = 1
				self.score += 10
			elif self.Y_cood>200 and check4 == 1:
				check4 = 2
				self.score += 10
			elif self.Y_cood>300 and check4 == 2:
				check4 = 3
				self.score += 10
			elif self.Y_cood>400 and check4 == 3:
				check4 = 4
				self.score += 10
			elif self.Y_cood>500 and check4 == 4:
				check4 = 5
				self.score += 10
			elif self.Y_cood>600 and check4 == 5:
				check4 = 6
				self.score += 10
		return	

class Obstacle():
	def __init__(self, x, y):
		self.X_cood = x
		self.Y_cood = y
		return

class FixedObstacle(Obstacle):
	def __init__(self,x,y):
		super(FixedObstacle, self).__init__(x, y)
		return

class MovingObstacle(Obstacle):
	def __init__(self,x, y):
		super(MovingObstacle, self).__init__(x, y)
		self.X_velocity = 0.3
		return

	def move(self):
		if self.X_cood > 864:
			self.X_cood = 0
		self.X_cood += self.X_velocity
		return 

	def change_speed(self):
		self.X_velocity=0.6


blocks = []
no_of_blocks=random.randint(8,10)
for i in range(no_of_blocks):
	k = (i*100-15)
	if k > 585:
		k = 670 - k
	j = random.randint(0, 736)
	if(k == 85 or k == 585):
		while(j > 350 and j < 450 ):
			j = random.randint(0, 736)
	blocks += [FixedObstacle(j, k)]

ships = []
no_of_ships=random.randint(6,10)
for i in range(no_of_ships):
	k=(i*100+30)
	if k > 530:
		k = k-600
	ships += [MovingObstacle(random.randint(0,736), k)]

running = False
hold=True