#Create an array of surfaces, each look updates the colour of all the squares as the square moves through the path.
import pygame, sys, math, time
from pygame.locals import *
import time
import random
pygame.init()

screenwidth = 800
length = 8
sleepTime = 1

#find best game window value
scrnwdth = length*int(math.ceil(screenwidth/length))

# Game window
surface = pygame.display.set_mode((scrnwdth, scrnwdth), 0, 32)
pygame.display.set_caption('Square Walking')

#Image
picture_Slice = pygame.image.load("River.jpg")

#Each square width will be
w = scrnwdth/length
mv = w

#Other constants
xm = int(length/2)
ym = int(length/2)

#Create square grid array for the background
squareMatrix = [[100 for x in range(length)] for x in range(length)]

#Create length*length number of square surfaces and place them randomly on the screen
squareMovement = [[[random.randint(0, int(length-1))*w, random.randint(0, int(length-1))*w] for x in range(length)] for x in range(length)]
print squareMovement

"""Game loop----------------------------------------------------------------"""

#Game loop and X quite
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#Refresh the surface
	surface.fill((125, 125, 125))#Blit the image

	#Check each value for the movement, and move it if necessary.
	for j in range(length):
		for k in range(length):
			rand = random.randint(0, 50)
			if rand > 0:
				if squareMovement[j][k][0] == j*w:
					pass
				elif squareMovement[j][k][0] < j*w:
					squareMovement[j][k][0] = squareMovement[j][k][0] + mv
				elif squareMovement[j][k] > j*w:
					squareMovement[j][k][0] = squareMovement[j][k][0] - mv

				if squareMovement[j][k][1] == k*w:
					pass
				elif squareMovement[j][k][1] < k*w:
					squareMovement[j][k][1] = squareMovement[j][k][1] + mv
				elif squareMovement[j][k] > k*w:
					squareMovement[j][k][1] = squareMovement[j][k][1] - mv
			elif rand == 0:
				squareMovement[j][k][0] = squareMovement[j][k][0] + mv*math.pow((-1), (random.randint(1, 2)))
				squareMovement[j][k][1] = squareMovement[j][k][1] + mv*math.pow((-1), (random.randint(1, 2)))

	#Update the colours of each square
	for j in range(length):
		for k in range(length):
			m = (-1)*(math.pow((-1), (k + j)) - 1)/2
			square_Surface = (pygame.Surface((w, w), pygame.SRCALPHA))
			square_Surface.fill((math.pow(255, m), math.pow(255, m), math.pow(255, m)))
			#Blit the image
			#square_Surface.blit(picture_Slice, (0, 0), (j*w, k*w, w, w))
			surface.blit(square_Surface, ((squareMovement[j][k][0], squareMovement[j][k][1])))
	#Update
	#t += 1

	pygame.display.update()
	time.sleep(sleepTime)