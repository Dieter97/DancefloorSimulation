from random import shuffle

import numpy as np
import pygame

from Agent import Agent

class Grid:

    def __init__(self,numberofAgents,width,height):
        self.numAgents = numberofAgents
        self.dancers = [Agent("SIM",np.random.randint(0,width),np.random.randint(0,height)) for i in range(numberofAgents)]
        print()

    def draw(self,screen):
        for i in range(self.numAgents):
             pygame.draw.circle(screen,  self.dancers[i].getColor(), (self.dancers[i].posX,  self.dancers[i].posY), 15)

    def updateDancers(self):
        """
        Changes the dancers' (agents) like rates
        """
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
        """
        Gets all votes from all dancers
        :param genre the currently playing genre
        :return a list with all votes
        """
        result = []
        for i in range(self.x):
            for j in range(self.y):
                result.append(self.dancers[i][j].vote(genre))
        return result