import pygame
import numpy as np
import time

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rows = WIDTH
columns = HEIGHT
screen_size = rows*columns
color = (226, 245, 241)
x_offset = rows / 2
y_offset = columns / 2

A, B = 0, 0
R1, R2 = 100, 200

def circleNates(radius, center=[R2, 0, 0], spacing=10):
    posCircle = []
    for theta in range(0, 629, spacing):
        xyz = np.add(center, [radius*np.cos(theta), radius*np.sin(theta), 0])
        posCircle.append(xyz)
    return posCircle

def torusNates(positions, spacing=10):
    posDonut = []
    for phi in range(0, 314, spacing):
        xyz = [positions[0]*np.cos(phi), 
               positions[1], 
               -positions[0]*np.sin(phi)]
        posDonut.append(xyz)
    return posDonut

cir = circleNates(R1)
don = []
# for i in cir:
#     don.append(torusNates(i))

# print(don[0])

run = True

while run:
    for i in cir:
        nate = i[:-1]
        # pygame.draw.circle(screen, (250, 250, 250), (nate[0]+x_offset, nate[1]+y_offset), 2)
        for j in torusNates(i):
            dnate = j[:-1]
            if j[2]>0:
                pygame.draw.circle(screen, color, (dnate[0]+x_offset, dnate[1]+y_offset), 1)
            # else: pygame.draw.circle(screen, (200, 200, 0), (dnate[0]+x_offset, dnate[1]+y_offset), 1)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

pygame.quit()