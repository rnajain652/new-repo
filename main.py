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

def isCollision(X1,Y1,X2,Y2):
	x1 = X1 + 12
	x2 = X2 + 32
	y1 = Y1 + 12
	y2 = Y2 + 32

	distance=math.sqrt(math.pow(x1 - x2, 2)+ math.pow(y1- y2, 2))

	if distance < 44:
		return  True
	else:
		return False

font = pygame.font.Font("freesansbold.ttf",32)

def gameover(p,ship):
	pygame.draw.rect(screen,(0,0,0,127),(50,150,700,300))
	text = font.render("GAME OVER", True, (255,0,0))
	screen.blit(text,(300,300))
	p.velocity = 0
	for i in range(len(ship)):
		ship[i].X_velocity = 0
		p.X_cood = 0
		p.Y_cood = 400

class Player:
	def __init__(self):
		self.X_cood = 400
		self.Y_cood = 600
		self.velocity = 0.3
		return

	def move(self, pressed_key):

		if self.X_cood < self.velocity:
			self.X_cood = 0
		if self.X_cood >= 768:
			self.X_cood = 768

		if self.Y_cood < self.velocity:
			self.Y_cood = 0
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
running=True
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
		collide=isCollision(p1.X_cood, p1.Y_cood, ships[i].X_cood, ships[i].Y_cood)
		if collide == True:
			gameover(p1,ships)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

	key=pygame.key.get_pressed()
	p1.move(key)
	screen.blit(playerImg,(p1.X_cood,p1.Y_cood))

	for i in range(len(ships)):
		collide=isCollision(p1.X_cood, p1.Y_cood, ships[i].X_cood, ships[i].Y_cood)
		if collide == True:
			gameover(p1,ships)

	for i in range(len(blocks)):
		collide=isCollision(p1.X_cood, p1.Y_cood, blocks[i].X_cood, blocks[i].Y_cood)
		if collide == True:
			gameover(p1,ships)

	pygame.display.update()