import pygame

from Agent import Agent

class Grid:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dancers = [[Agent() for i in range(x)] for j in range(y)]
        print(self.dancers)

    def draw(self,screen,width,heigth):
        for i in range(0,self.x):
            for j in range(0,self.y):
                rect = pygame.Rect(i*width, j*heigth, width, heigth)
                pygame.draw.rect(screen,  self.dancers[i][j].getColor(), rect)

    def updateDancers(self):
        dirs = [[0,-1],[0,1],[1,0],[-1,0]]
        for i in range(0,self.x):
            for j in range(0,self.y):
                neighbours = []
                for dir in dirs:
                    try:
                        neighbours.append(self.dancers[i+dir[0]][j+dir[1]])
                    except IndexError:
                        continue
                self.dancers[i][j].calculateNewLikeRates(neighbours)