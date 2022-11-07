import pygame
import numpy as np
import math

pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

rows = WIDTH
columns = HEIGHT
screen_size = rows*columns
alpha = 10
color = (200, 200, 200, alpha)
x_offset = rows / 2
y_offset = columns / 2

A, B = 10, 10
R1, R2 = 100, 200
spacing = 40 #21

def circleNates(radius, center=[R2, 0, 0], spacing=10):
    posCircle = []
    for theta in range(0, 629, spacing):
        xyz = np.add(center, [radius*np.cos(theta/100), radius*np.sin(theta/100), 0])
        posCircle.append(xyz)
    return posCircle

def torusNates(positions, spacing=10):
    posDonut = []
    for phi in range(0, 2*314, spacing):
        xyz = [positions[0]*np.cos(phi/100), 
               positions[1], 
               -positions[0]*np.sin(phi/100)]
        posDonut.append(xyz)
    return posDonut

def torus(R1, R2, center=[0, 0, 0], spacing=10):
    positions = []
    for theta in range(0, 629, spacing):
        for phi in range(0, 629, spacing):
            xyz = [(R2+R1*np.cos(theta/100))*np.cos(phi/100),
                    R1*np.sin(theta/100), 
                    -(R2+R1*np.cos(theta/100)*np.sin(phi/100))]
            positions.append(xyz)
    return positions

def zBuffer(R1, R2, zPosition, luminance=[50, 200]):
    divs = int((luminance[1]-luminance[0])/(R1+R2)*100)
    lumins = [i/100 for i in range(luminance[0]*100, luminance[1]*100, divs)]
    weight = zPosition
    if weight >= 0: return int(lumins[math.floor(weight)])
    else: return int(lumins[::-1][math.floor(abs(weight))])

def drawCircle(positions):
    for i in positions:
        # alpha = zBuffer(R1, R2, i[-1])
        color = (200, 200, 200) #(alpha, alpha, alpha)
        pygame.draw.circle(screen, color, (i[0]+x_offset, i[1]+y_offset), 2)


def rotate(positions, A, B):
    X = ([1, 0, 0], [0, np.cos(A), np.sin(A)], [0, -np.sin(A), np.cos(A)])
    Y = ([np.cos(B), np.sin(B), 0], [-np.sin(B), np.cos(B), 0], [0, 0, 1])
    rotate = np.dot(X, Y)
    for i in range(len(positions)):
        positions[i] = np.dot(i, rotate)
    
    return positions
# print(don[0])
# cir = circleNates(R1, spacing=spacing)
# don = [torusNates(i) for i in cir]
# print(len(cir), len(don), len(don[0]))
# l = [i[-1] for i in don]
# print(zBuffer(R1, R2, min(l)))
# print(min(l), max(l), len(l))
cir = torus(R1, R2)
# ls = rotate(cir, A, B)
# print(ls[3])
i = 0
run = True

while run:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    # pos = cir
    # i += 1
    # if i > 15:
    #     i=0
    # pos = don[i]
    # pygame.time.wait(100)
    drawCircle(cir)

    # cir = rotate(cir, A, B)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

pygame.quit()