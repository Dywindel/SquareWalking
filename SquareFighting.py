#Create a grid of squares that react to different colour squares aroud them
import pygame, sys, math, time
from pygame.locals import *
import time
import random
pygame.init()

screenwidth = 1000
length = 100
numberOfGroups = 2
sleepTime = 0.01

#find best game window value
scrnwdth = length*int(math.ceil(screenwidth/length))

# Game window
surface = pygame.display.set_mode((scrnwdth, scrnwdth), 0, 32)
pygame.display.set_caption('Square Fighting')

#Each square width will be
w = scrnwdth/length
#Angle of the circle
phi = 360/numberOfGroups

#Create square grid array for the background
squareMatrix = [[255 for x in range(length)] for x in range(length)]

#Store position and colour
squareData = [[[[0 ,0], [0, 0, 0]] for x in range(length)] for x in range(length)]

#Move them into start positions
for j in range(length):
	for k in range(length):
		squareData[j][k][0][0] = j*w
		squareData[j][k][0][1] = k*w

'''
#Create the divided colours on either side of the screen
for psy in range(phi, 361, phi):
	print psy
	xIMin = int((length/2)*(math.cos(psy-phi)))
	yIMin = int((length/2)*(math.sin(psy-phi)))
	xIMax = int((length/2)*(math.cos(psy)))
	yIMax = int((length/2)*(math.sin(psy)))
	rCol = int(abs(250*math.cos(psy)))
	gCol = int(abs(250*math.sin(psy)))
	print str(xIMax)
'''
'''
#Calculate a colour based on phi
for psy in range(phi, 361, phi):
	rCol = int(abs(250*math.cos(psy)))
	gCol = int(abs(250*math.sin(psy)))
	#Calculate phi from x and y
'''

for j in range(length):
	for k in range(length):
		#Calculate angle
		angle = (180/math.pi)*math.atan2(k-length/2, j-length/2) + 180
		for psy in range(0, 360, phi):
			if abs(angle - psy) < phi:
				if (0 <= angle < 90):
					squareData[j][k][1] = [((360-psy)*255)/(360), 0, 0]
				elif (90 <= angle < 180):
					squareData[j][k][1] = [0, (psy*255)/(360), 0]
				elif (180 <= angle < 270):
					squareData[j][k][1] = [0, 0, (psy*255)/(360)]
				elif (270 <= angle < 360):
					squareData[j][k][1] = [((psy)*255)/(360), ((psy)*255)/(360), 0]

'''
for j in range(length):
	for k in range(length):
		if j >= length/2 and k >= length/2:
			squareData[j][k][1] = [255, 0, 0]
		elif k >= length/2:
			squareData[j][k][1] = [0, 0, 255]
		elif j >= length/2:
			squareData[j][k][1] = [0, 255, 0]
		else:
			squareData[j][k][1] = [255, 255, 0]
'''

#Game Loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#Refresh the surface
	surface.fill((255, 255, 255))

	#If the colour is black, nothing happens
	#Set how the colours change
	#Facing right only
	for j in range(length-1):
		for k in range(length):
			#If your colour is different, switch with a random probability
			if squareData[j][k][1] != squareData[j+1][k][1] and squareData[j+1][k][1] != [0, 0, 0]:
				if random.randint(0, 1) == 1:
					squareData[j][k][1] = squareData[j+1][k][1]
					pass

	#Facing left only
	for j in range(length-1, 0, -1):
		for k in range(length):
			if squareData[j][k][1] != squareData[j-1][k][1] and squareData[j-1][k][1] != [0, 0, 0]:
				if random.randint(0, 1) == 1:
					squareData[j][k][1] = squareData[j-1][k][1]
					pass

	#Facing Up only
	for j in range(length):
		for k in range(length-1):
			if squareData[j][k][1] != squareData[j][k+1][1] and squareData[j][k+1][1] != [0, 0, 0]:
				if random.randint(0, 1) == 1:
					squareData[j][k][1] = squareData[j][k+1][1]
					pass

	#Facing Down only
	for j in range(length):
		for k in range(length-1, 0, -1):
			if squareData[j][k][1] != squareData[j][k-1][1] and squareData[j][k-1][1] != [0, 0, 0]:
				if random.randint(0, 1) == 1:
					squareData[j][k][1] = squareData[j][k-1][1]
					pass

	#Update the colours of each square
	for j in range(length):
		for k in range(length):
			square_Surface = (pygame.Surface((w, w), pygame.SRCALPHA))
			square_Surface.fill((squareData[j][k][1][0], squareData[j][k][1][1], squareData[j][k][1][2], squareMatrix[j][k]))
			surface.blit(square_Surface, (squareData[j][k][0]))
	#Ipdate
	#i += 1

	pygame.display.update()
	time.sleep(sleepTime)