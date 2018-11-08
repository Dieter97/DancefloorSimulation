from random import shuffle

import pygame

from Agent import Agent

class Grid:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dancers = [[Agent("SIM") for i in range(y)] for j in range(x)]
        print()

    def draw(self,screen,width,heigth):
        for i in range(self.x):
            for j in range(self.y):
                rect = pygame.Rect(i*width, j*heigth, width, heigth)
                pygame.draw.rect(screen,  self.dancers[i][j].getColor(), rect)

    def updateDancers(self):
        dirs = [[0,-1],[0,1],[1,0],[-1,0]]
        for i in range(self.x):
            for j in range(self.y):
                neighbours = []
                shuffle(dirs)
                for dir in dirs:
                    if i == 0 and dir[0] == -1 or j == 0 and dir[1] == -1:
                        continue
                    try:
                        neighbours.append(self.dancers[i+dir[0]][j+dir[1]])
                    except IndexError:
                        pass
                self.dancers[i][j].calculateNewLikeRates(neighbours)

    def getDancersVotes(self,genre):
        result = []
        for i in range(self.x):
            for j in range(self.y):
                result.append(self.dancers[i][j].vote(genre))
        return result