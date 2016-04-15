#Create an array of surfaces, each look updates the colour of all the squares as the square moves through the path.
import pygame, sys, math, time
from pygame.locals import *
import time
import random
pygame.init()

screenwidth = 800
length = 30
sleepTime = 0.02

#find best game window value
scrnwdth = length*int(math.ceil(screenwidth/length))

# Game window
surface = pygame.display.set_mode((scrnwdth, scrnwdth), 0, 32)
pygame.display.set_caption('Square Walking')

#Each square width will be
w = scrnwdth/length

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
	surface.fill((255, 255, 255))

	#Check each value for the movement, and move it if necessary.
	for j in range(length):
		for k in range(length):
			if squareMovement[j][k][0] == j*w:
				pass
			elif squareMovement[j][k][0] < j*w:
				squareMovement[j][k][0] = squareMovement[j][k][0] + 1
			elif squareMovement[j][k] > j*w:
				squareMovement[j][k][0] = squareMovement[j][k][0] - 1

			if squareMovement[j][k][1] == k*w:
				pass
			elif squareMovement[j][k][1] < k*w:
				squareMovement[j][k][1] = squareMovement[j][k][1] + 1
			elif squareMovement[j][k] > k*w:
				squareMovement[j][k][1] = squareMovement[j][k][1] - 1

	#Update the colours of each square
	for j in range(length):
		for k in range(length):
			pygame.draw.circle(surface, (((length-j)*250/length), (k*250/length), int((length-k)*j*250/(length*length))), (squareMovement[j][k][0], squareMovement[j][k][1]), w/2)
	#Ipdate
	#i += 1

	pygame.display.update()
	time.sleep(sleepTime)