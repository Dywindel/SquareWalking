import pygame, sys, math, time
from pygame.locals import *
import time
import random
pygame.init()

scrnwdthx = 800
scrnwdthy = 800

# Game window
surface = pygame.display.set_mode((scrnwdthx, scrnwdthy,), 0, 32)
pygame.display.set_caption('Square Walking')

#Set Font
basicFont = pygame.font.SysFont(None, 48)

#Lets get some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 128)
ORANGE = (255, 100, 0)
GREY = (128, 128, 128)
COLOUR = (0, 0, 0)

#Constants
w = 50
sleepTime = 0.01

#Arrays
i = 0
x = []
y = []
xm = 0
ym = 0
xmove = 0
ymove = 0
rect = []

"""Game loop----------------------------------------------------------------"""

#Game loop and X quite
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	rand = random.randint(0, 1)
	if rand == 0:
		xm += 1
		xmove = xm*w
		if xmove > scrnwdthx:
			xmove = 0
			xm = 0
	if rand == 1:
		ym += 1
		ymove = ym*w
		if ymove > scrnwdthy:
			ymove = 0
			ym = 0

	x.append(xmove)
	y.append(ymove)

	#Refresh the surface
	surface.fill(WHITE)

	#rect.append((x[i], y[i], w, w))
	for j in range(i):
		#pygame.draw.rect(surface, pygame.Color(100, 100, 100, 128), (x[j], y[j], w, w))
		#Try drawing a separate surface instead
		square_Surface = (pygame.Surface((w, w), pygame.SRCALPHA))
		square_Surface.fill((0, 0, 0, 30))
		surface.blit(square_Surface, (x[j], y[j]))

	#Ipdate
	i += 1

	pygame.display.update()
	time.sleep(sleepTime)


