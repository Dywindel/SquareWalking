#Create an array of surfaces, each look updates the colour of all the squares as the square moves through the path.
import pygame, sys, math, time
from pygame.locals import *
import time
import random
import math
pygame.init()

screenwidth = 800
length = 30
sleepTime = 0.01

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
i = 0

#Create square grid array for the background
squareMatrix = [[100 for x in range(length*2)] for x in range(length*2)]
squareLocation = [[[0, 0] for x in range(length*2)] for x in range(length*2)]

#Create length*length number of square surfaces and place them randomly on the screen
for j in range(length*2):
	for k in range(length*2):
		squareLocation[j][k][0] = (j*w) - length*w/2
		squareLocation[j][k][1] = (k*w) - length*w

"""Game loop----------------------------------------------------------------"""

#Game loop and X quite
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#Refresh the surface
	surface.fill((255, 255, 255))

	#Change all [k] values depending on time due to sine function
	for j in range(length*2):
		for k in range(length*2):
			squareLocation[j][k][1] = squareLocation[j][k][1] + int(float(math.sin(math.pi*i*sleepTime/2)*5*math.sin(math.pi*i/100*length)))

	#Update the colours of each square
	for j in range(length*2):
		for k in range(length*2):
			pygame.draw.circle(surface, ((((length*2)-j)*250/(length*2)), (k*250/(length*2)), int(((length*2)-k)*j*250/(length*length*4))), (squareLocation[j][k][0], squareLocation[j][k][1]), w/2)
	#Ipdate
	i += 1

	pygame.display.update()
	time.sleep(sleepTime)