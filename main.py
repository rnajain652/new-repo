import pygame
import random
import math

#initialize pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,630))

#Title and Icon
pygame.display.set_caption("River Crossing")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load("player.png")
fixed_obstacle1Img=pygame.image.load("fixed_obstacle1.png")
shipImg=pygame.image.load("ship.png")

player_status = 1
player1_score = 0
player2_score = 0

def isCollision(X1,Y1,X2,Y2):
	if((X2<=(X1+24)<=(X2+64) and Y2 <= Y1 <= (Y2 +64)) or (X2 <= (X1+24) <= (X2+64) and Y2 <= (Y1+24) <= (Y2 +64)) or (X2 <= (X1+24) <= (X2+64) and Y2 <= Y1 <= (Y2 +64)) or (X2 <= X1 <= (X2+64) and Y2 <= (Y1+24) <= (Y2 +64))):
	#	print("collide")
		return True
	else:
		return False

#	x1 = X1 + 12
#	x2 = X2 + 32
#	y1 = Y1 + 12
#	y2 = Y2 + 32

#	distance=math.sqrt(math.pow(x1 - x2, 2)+ math.pow(y1- y2, 2))

#	if distance < 44:
#		return  True
#	else:
#		return False

def end1(p):
	global playerImg 
	global player_status
	p.X_cood=400
	p.Y_cood=0
	player_status+=1
	print(player_status)
	playerImg = pygame.image.load("player2.png")

def end2(p):
	global playerImg
	global player_status
	p.X_cood=400
	p.Y_cood=600
	player_status+=1
	playerImg = pygame.image.load("player.png")

font = pygame.font.Font("freesansbold.ttf",32)

class Player:
	def __init__(self):
		self.X_cood = 400
		self.Y_cood = 600
		self.velocity = 0.3
		self.score=0
		return

	def move(self, pressed_key):
		global player_status

		if self.X_cood < self.velocity:
			self.X_cood = self.velocity
		if self.X_cood >= 768:
			self.X_cood = 768

		if self.Y_cood < self.velocity:
			self.Y_cood = self.velocity
		if self.Y_cood >= 598:
			self.Y_cood = 598		
		
		if pressed_key[pygame.K_LEFT] == True:
			self.X_cood -= self.velocity

		elif pressed_key[pygame.K_RIGHT] == True:
			self.X_cood += self.velocity

		elif pressed_key[pygame.K_UP] == True:
			self.Y_cood -= self.velocity

		elif pressed_key[pygame.K_DOWN] == True:
			self.Y_cood += self.velocity

		if player_status%2 == 1:
			if self.Y_cood>100 :
				self.score += 5
			elif self.Y_cood%100 == 30:
				self.score += 10 
		print("\n", player_status, "\t", self.score)
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
	blocks += [FixedObstacle(random.randint(0, 736), k)]

ships = []
no_of_ships=random.randint(6,10)
for i in range(no_of_ships):
	k=(i*100+30)
	if k > 530:
		k = k-600
	ships += [MovingObstacle(random.randint(0,736), k)]

p1 = Player()

#Game Loop
running = False
hold=True
while hold:
#	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			hold=False
		text = font.render("TO START PRESS ANY KEY", True, (255,255,255))
		screen.blit(text,(200,250))
		if event.type == pygame.KEYDOWN:
			running=True
			hold=False

	pygame.display.update()

while running:

	screen.fill((51,153,255))

	slab_y=0
	for i in range (0,6):
		pygame.draw.rect(screen,(153,76,0),(0,slab_y,800,30))
		slab_y += 100

	pygame.draw.rect(screen,(153,76,0),(0,slab_y,800,30))

	for i in range(len(blocks)):
		screen.blit(fixed_obstacle1Img,(blocks[i].X_cood,blocks[i].Y_cood))

	screen.blit(playerImg,(p1.X_cood,p1.Y_cood))

	for i in range(len(ships)):
		ships[i].move()
		screen.blit(shipImg,(ships[i].X_cood, ships[i].Y_cood))

	for i in range(len(ships)):
		if isCollision(p1.X_cood, p1.Y_cood, ships[i].X_cood, ships[i].Y_cood):

			if player_status==4:
				player2_score=p1.score
				p1.score=0		
				running=False
				hold2=True

			elif player_status%2 == 1:
				player1_score=p1.score
				p1.score=0
				end1(p1)
			elif player_status%2 == 0:
				player2_score=p1.score
				p1.score=0
				if player_status==2:
					for j in range(len(ships)):
						ships[j].change_speed()
				end2(p1)
		#	print(player_status)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	key=pygame.key.get_pressed()
	p1.move(key)
	screen.blit(playerImg,(p1.X_cood,p1.Y_cood))

	for i in range(len(ships)):
		if isCollision(p1.X_cood, p1.Y_cood, ships[i].X_cood, ships[i].Y_cood) :
			if player_status==4:
				player2_score=p1.score
				p1.score=0
				running=False
				hold2=True			
			elif player_status%2 ==1:
				player1_score=p1.score
				p1.score=0
				end1(p1)
			elif player_status%2 ==0:
				player2_score=p1.score
				p1.score=0
				if player_status==2:
					for j in range(len(ships)):
						ships[j].change_speed()
				end2(p1)

		#	print(player_status)

	for i in range(len(blocks)):
		if isCollision(p1.X_cood, p1.Y_cood, blocks[i].X_cood, blocks[i].Y_cood) :
			if player_status==4:
				player2_score=p1.score
				p1.score=0
				running=False
				hold2=True
			elif player_status%2 ==1:
				player1_score=p1.score
				p1.score=0
				end1(p1)
			elif player_status%2==0:
				player2_score=p1.score
				p1.score=0
				if player_status==2:
					for j in range(len(ships)):
						ships[j].change_speed()
				end2(p1)	

		#	print(player_status)
	#print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')

	pygame.display.update()

while hold2:
	screen.fill((255,0,0))
	text = font.render("GAME OVER", True, (0,0,0))
	screen.blit(text,(350,250))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			hold2=False

	pygame.display.update()