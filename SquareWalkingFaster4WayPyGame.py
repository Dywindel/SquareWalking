#Create an array of surfaces, each look updates the colour of all the squares as the square moves through the path.
import pygame, sys, math, time
from pygame.locals import *
import time
import random
pygame.init()

screenwidth = 800
length = 30
sleepTime = 0
opacityStep = 40

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

#Create square grid array
squareMatrix = [[40 for x in range(length)] for x in range(length)]


"""Game loop----------------------------------------------------------------"""

#Game loop and X quite
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#Generate random movement down and right
	rand = random.randint(0, 3)
	if rand == 0:
		#Increase x
		xm = xm + 1
		if xm > length - 1:
			xm = 0
	if rand == 1:
		#increase y
		ym = ym + 1
		if ym > length - 1:
			ym = 0
	if rand == 2:
		#Increase x
		xm = xm - 1
		if xm < 0:
			xm = length - 1
	if rand == 3:
		#increase y
		ym = ym - 1
		if ym < 0:
			ym = length - 1

	#Change transparency depending on location
	squareMatrix[xm][ym] = squareMatrix[xm][ym] + opacityStep
	if squareMatrix[xm][ym] > 255:
		squareMatrix[xm][ym] = 255

	#Refresh the surface
	surface.fill((255, 255, 255))

	#Update the colours of each square
	for j in range(length):
		for k in range(length):
			square_Surface = (pygame.Surface((w, w), pygame.SRCALPHA))
			square_Surface.fill((((length-j)*250/length), (k*250/length), int((length-k)*j*250/(length*length)), squareMatrix[j][k]))
			surface.blit(square_Surface, (j*w, k*w))
	#Ipdate
	#i += 1

	pygame.display.update()
	time.sleep(sleepTime)