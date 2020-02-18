import pygame
import random
import math
import time
from config import *

#initialize pygame
pygame.init()

#create the screen
#screen=pygame.display.set_mode((800,630))

#Title and Icon
# pygame.display.set_caption("River Crossing")
# icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Player
# playerImg=pygame.image.load("player.png")
# fixed_obstacle1Img=pygame.image.load("fixed_obstacle1.png")
# shipImg=pygame.image.load("ship.png")

# player_status = 1
# player1_score = 0
# player2_score = 0
# player1_time = 0
# player2_time = 0
# check1=0
# check2=0
# check3=0
# check4=0

def isCollision(X1,Y1,X2,Y2):
	if((X2<=(X1+24)<=(X2+64) and Y2 <= Y1 <= (Y2 +64)) or (X2 <= (X1+24) <= (X2+64) and Y2 <= (Y1+24) <= (Y2 +64)) or (X2 <= (X1+24) <= (X2+64) and Y2 <= Y1 <= (Y2 +64)) or (X2 <= X1 <= (X2+64) and Y2 <= (Y1+24) <= (Y2 +64))):
	#	print("collide")
		return True
	else:
		return False

def end1(p):
	global playerImg 
	global player_status
	global player1_score
	global check1
	global check3
	global player1_time
	global start_time
	player1_time += (time.time() - start_time)
	start_time = time.time()
	p.X_cood=400
	p.Y_cood=0
	player_status+=1
	check1=0
	check3=0
	player1_score += p.score
	p.score=0
	#print(player_status)
	playerImg = pygame.image.load("player2.png")


def end2(p):
	global playerImg
	global player_status
	global player2_score
	global check2
	global check4
	global player2_time
	global start_time
	player2_time += (time.time() - start_time)
	start_time = time.time()
	p.X_cood=400
	p.Y_cood=600

	player_status+=1

	if player_status == 4:
		running=False
		hold2=True

	check2=0
	check4=0
	player2_score+=p.score
	p.score=0
	playerImg = pygame.image.load("player.png")

font = pygame.font.Font("freesansbold.ttf",32)

# class Player:
# 	def __init__(self):
# 		self.X_cood = 400
# 		self.Y_cood = 600
# 		self.velocity = 0.3
# 		self.score=0
# 		return

# 	def move(self, pressed_key):
# 		global player_status
# 		global check1
# 		global check2
# 		global check3
# 		global check4

# 		if self.X_cood < self.velocity:
# 			self.X_cood = self.velocity
# 		if self.X_cood >= 768:
# 			self.X_cood = 768

# 		if self.Y_cood < self.velocity:
# 			self.Y_cood = self.velocity
# 		if self.Y_cood >= 600:
# 			self.Y_cood = 600		
		
# 		if pressed_key[pygame.K_LEFT] == True:
# 			self.X_cood -= self.velocity

# 		elif pressed_key[pygame.K_RIGHT] == True:
# 			self.X_cood += self.velocity

# 		elif pressed_key[pygame.K_UP] == True:
# 			self.Y_cood -= self.velocity

# 		elif pressed_key[pygame.K_DOWN] == True:
# 			self.Y_cood += self.velocity

# 		if player_status%2 == 1:
# 			if self.Y_cood<600 and check1 == 0:
# 				check1 = 1
# 				self.score += 5
# 			elif self.Y_cood<500 and check1 == 1:
# 				check1 = 2
# 				self.score += 5
# 			elif self.Y_cood<400 and check1 == 2:
# 				check1 = 3
# 				self.score += 5
# 			elif self.Y_cood<300 and check1 == 3:
# 				check1 = 4
# 				self.score += 5
# 			elif self.Y_cood<200 and check1 == 4:
# 				check1 = 5
# 				self.score += 5
# 			elif self.Y_cood<100 and check1 == 5:
# 				check1 = 6
# 				self.score += 5	

# 			if self.Y_cood<530 and check3 == 0:
# 				check3 = 1
# 				self.score += 10
# 			elif self.Y_cood<430 and check3 == 1:
# 				check3 = 2
# 				self.score += 10
# 			elif self.Y_cood<330 and check3 == 2:
# 				check3 = 3
# 				self.score += 10
# 			elif self.Y_cood<230 and check3 == 3:
# 				check3 = 4
# 				self.score += 10
# 			elif self.Y_cood<130 and check3 == 4:
# 				check3 = 5
# 				self.score += 10
# 			elif self.Y_cood<30 and check3 == 5:
# 				check3 = 6
# 				self.score += 10

# 		elif player_status%2 == 0:
# 			if self.Y_cood>30 and check2 == 0:
# 				check2 = 1
# 				self.score += 5
# 			elif self.Y_cood>130 and check2 == 1:
# 				check2 = 2
# 				self.score += 5
# 			elif self.Y_cood>230 and check2 == 2:
# 				check2 = 3
# 				self.score += 5
# 			elif self.Y_cood>330 and check2 == 3:
# 				check2 = 4
# 				self.score += 5
# 			elif self.Y_cood>430 and check2 == 4:
# 				check2 = 5
# 				self.score += 5
# 			elif self.Y_cood>530 and check2 == 5:
# 				check2 = 6
# 				self.score += 5	

# 			if self.Y_cood>100 and check4 == 0:
# 				check4 = 1
# 				self.score += 10
# 			elif self.Y_cood>200 and check4 == 1:
# 				check4 = 2
# 				self.score += 10
# 			elif self.Y_cood>300 and check4 == 2:
# 				check4 = 3
# 				self.score += 10
# 			elif self.Y_cood>400 and check4 == 3:
# 				check4 = 4
# 				self.score += 10
# 			elif self.Y_cood>500 and check4 == 4:
# 				check4 = 5
# 				self.score += 10
# 			elif self.Y_cood>600 and check4 == 5:
# 				check4 = 6
# 				self.score += 10
# 			#elif self.Y_cood%100 == 30:
# 			#	self.score += 10 
# 		#print("\n", player_status, "\t", self.score, "\t", check1, "\t", self.Y_cood)
# 		return	

# class Obstacle():
# 	def __init__(self, x, y):
# 		self.X_cood = x
# 		self.Y_cood = y
# 		return

# class FixedObstacle(Obstacle):
# 	def __init__(self,x,y):
# 		super(FixedObstacle, self).__init__(x, y)
# 		return

# class MovingObstacle(Obstacle):
# 	def __init__(self,x, y):
# 		super(MovingObstacle, self).__init__(x, y)
# 		self.X_velocity = 0.3
# 		return

# 	def move(self):
# 		if self.X_cood > 864:
# 			self.X_cood = 0
# 		self.X_cood += self.X_velocity
# 		return 

# 	def change_speed(self):
# 		self.X_velocity=0.6

# blocks = []
# no_of_blocks=random.randint(8,10)
# for i in range(no_of_blocks):
# 	k = (i*100-15)
# 	if k > 585:
# 		k = 670 - k
# 	j = random.randint(0, 736)
# 	if(k == 85 or k == 585):
# 		while(j > 350 and j < 450 ):
# 			j = random.randint(0, 736)
# 	blocks += [FixedObstacle(j, k)]

# ships = []
# no_of_ships=random.randint(6,10)
# for i in range(no_of_ships):
# 	k=(i*100+30)
# 	if k > 530:
# 		k = k-600
# 	ships += [MovingObstacle(random.randint(0,736), k)]

p1 = Player()
# start_time=time.time()

#Game Loop
# running = False
# hold=True
while hold:
#	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			hold=False
		text = font.render("PRESS ANY KEY TO START", True, (255,255,255))
		screen.blit(text, (200,250))
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

	msg = font.render("Player1_Score: " + str(player1_score) ,True ,(255 , 255 , 255))
	screen.blit(msg,(0,0))

	msg = font.render("Player2_Score: " + str(player2_score) ,True ,(255 , 255 , 255))
	screen.blit(msg,(500,600))

	if check1==6:
		end1(p1)

	if check2==6:
		end2(p1)

	for i in range(len(ships)):
		if isCollision(p1.X_cood, p1.Y_cood, ships[i].X_cood, ships[i].Y_cood):

			if player_status==4:
				player2_time += (time.time() - start_time)
				start_time = time.time()
				player2_score+=p1.score		
				running=False
				hold2=True

			elif player_status%2 == 1:
				end1(p1)
			elif player_status%2 == 0:
				if player_status==2:
					for j in range(len(ships)):
						ships[j].change_speed()
				end2(p1)
			print(player_status)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	key=pygame.key.get_pressed()
	p1.move(key)
	screen.blit(playerImg,(p1.X_cood,p1.Y_cood))

	for i in range(len(ships)):
		if isCollision(p1.X_cood, p1.Y_cood, ships[i].X_cood, ships[i].Y_cood) :
			if player_status==4:
				player2_time += (time.time() - start_time)
				start_time = time.time()	
				player2_score+=p1.score
				running=False
				hold2=True			
			elif player_status%2 ==1:
				end1(p1)
			elif player_status%2 ==0:
				if player_status==2:
					for j in range(len(ships)):
						ships[j].change_speed()
				end2(p1)

			print(player_status)

	for i in range(len(blocks)):
		if isCollision(p1.X_cood, p1.Y_cood, blocks[i].X_cood, blocks[i].Y_cood) :
			if player_status==4:
				player2_time += (time.time() - start_time)
				start_time = time.time()
				player2_score+=p1.score
				running=False
				hold2=True
			elif player_status%2 ==1:
				end1(p1)
			elif player_status%2==0:
				if player_status==2:
					for j in range(len(ships)):
						ships[j].change_speed()
				end2(p1)	

		show = font.render("Current_Score: " + str(p1.score) ,True ,(255 , 255 , 255))
		screen.blit(show,(500,0))


		#	print(player_status)
	#print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')

	pygame.display.update()

while hold2:
	screen.fill((255,0,0))
	text = font.render("GAME OVER", True, (0,0,0))
	screen.blit(text,(350,250))
	#print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')	
	
	#print("\nplayer1_time : ", player1_time , "\tplayer2_time : ", player2_time)

	if player1_score < player2_score:
	#	print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')
		text2 = font.render("WINNER:PLAYER 2",True,(0,0,0))
		screen.blit(text2,(300, 450))

	elif player1_score > player2_score:
	#	print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')
		text2 = font.render("WINNER:PLAYER 1",True,(0,0,0))
		screen.blit(text2,(300, 450))

	else:
		if player1_time < player2_time:
		#	print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')
			text2 = font.render("WINNER:PLAYER 1",True,(0,0,0))
			screen.blit(text2,(300, 450))

		elif player1_time > player2_time:
		#	print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')
			text2 = font.render("WINNER:PLAYER 1",True,(0,0,0))
			screen.blit(text2,(300, 450))			

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			hold2=False

	pygame.display.update()

print("player1_score : ", player1_score ,"\tplayer2_score : ", player2_score, end='\n')