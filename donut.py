import pygame
import numpy as np
import math
import random

pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

rows = WIDTH
columns = HEIGHT
screen_size = rows*columns
x_offset = rows / 2
y_offset = columns / 2

A, B = 0.04, 0.01 #A --> X rotation angle, B --> Y rotation angle
R1, R2 = 100, 200
spacing = 10 #21
radius = 2

lumMin, lumMax = 50, 255
lumWidth = int(100*(lumMax-lumMin)/(2*(R1+R2)))
maps = [i for i in range(lumMin*100, lumMax*100, lumWidth)]

def all_positions(R1, R2, spacing=10):
    positions = []
    for theta in range(0, 629, spacing):
        for phi in range(0, 629, spacing):
            x, y, z = (R2+R1*np.cos(theta/100))*np.cos(phi/100), R1*np.sin(theta/100), -(R2+R1*np.cos(theta/100))*np.sin(phi/100)
            positions.append([x, y, z])
    return positions

def surfNormals():
    pass

def zBuffer(zPos, lumMap):
    alpha = 200
    index = int(zPos+301)
    alpha = lumMap[index]/100
    return int(alpha)

def drawCircle(positions, radius=2):
    for i in positions:
        alpha = zBuffer(i[-1], maps)
        color = (alpha, alpha, alpha)
        pygame.draw.circle(screen, color, (i[0]+x_offset, i[1]+y_offset), radius)


def rotate(positions, A, B):
    X = ([1, 0, 0], [0, np.cos(A), np.sin(A)], [0, -np.sin(A), np.cos(A)])
    Y = ([np.cos(B), np.sin(B), 0], [-np.sin(B), np.cos(B), 0], [0, 0, 1])
    rotation = np.dot(X, Y)
    for i in range(len(positions)):
        positions[i] = np.dot(positions[i], rotation)
    
    return positions
    
cir = all_positions(R1, R2, spacing)
run = True

while run:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    
    # pygame.time.wait(200)
    drawCircle(cir, radius)
    cir = rotate(cir, A, B)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

pygame.quit()