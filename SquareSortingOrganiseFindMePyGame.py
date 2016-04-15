#Create an array of surfaces, each look updates the colour of all the squares as the square moves through the path.
import pygame, sys, math, time
from pygame.locals import *
import time
from PIL import Image
import random
pygame.init()

screenwidth = 800
length = 5
sleepTime = 0

#find best game window value
scrnwdth = length*int(math.ceil(screenwidth/length))

#Set Font
basicFont = pygame.font.SysFont("monospace", 12)

# Game window
surface = pygame.display.set_mode((scrnwdth, scrnwdth), 0, 32)
pygame.display.set_caption('Square Walking')

#Load an image
picture = pygame.image.load("River.jpg")
#crop the image


#Each square width will be
w = scrnwdth/length
mv = w/2

#Other constants
xm = int(length/2)
ym = int(length/2)

#Create square grid array for the background
squareMatrix = [[100 for x in range(length)] for x in range(length)]

#Create length*length number of square surfaces and place them randomly on the screen
squareMovement = [[[random.randint(0, int(length-1))*w, random.randint(0, int(length-1))*w, 0] for x in range(length)] for x in range(length)]

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
			if (squareMovement[j][k][0] == j*w) and (squareMovement[j][k][1] == k*w):
				pass
			else:
				squareMovement[j][k][2] += 1
				if squareMovement[j][k][0] < 0:
					squareMovement[j][k][0] = (length-1)*w
				elif squareMovement[j][k][0] > (length-1)*w:
					squareMovement[j][k][0] = 0
				elif squareMovement[j][k][1] < 0:
					squareMovement[j][k][1] = (length-1)*w
				elif squareMovement[j][k][1] > (length-1)*w:
					squareMovement[j][k][1] = 0
				else:
					if random.randint(0, 1) == 0:
						squareMovement[j][k][0] = squareMovement[j][k][0] + mv*math.pow((-1), (random.randint(1, 2)))
					else:
						squareMovement[j][k][1] = squareMovement[j][k][1] + mv*math.pow((-1), (random.randint(1, 2)))

	#Update the colours of each square
	for j in range(length):
		for k in range(length):
			square_Surface = (pygame.Surface((w, w), pygame.SRCALPHA))
			square_Surface.fill((((length-j)*250/length), (k*250/length), int((length-k)*j*250/(length*length)), squareMatrix[j][k]))
			phrase = str(squareMovement[j][k][2])
			text = basicFont.render(phrase, 1, (0, 0, 0))
			#Blit the image
			square_Surface.blit(picture, [1, 1])
			square_Surface.blit(text,  [1, 1])
			surface.blit(square_Surface, ((squareMovement[j][k][0], squareMovement[j][k][1])))
	#Ipdate
	#i += 1

	pygame.display.update()
	time.sleep(sleepTime)