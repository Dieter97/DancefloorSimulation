from random import shuffle

import numpy as np
import pygame

from Agent import Agent


class Grid:

    def __init__(self, numberofAgents, width, heigth):
        self.numAgents = numberofAgents
        self.width = width
        self.heigth = heigth
        self.dancers = [Agent("SIM", np.random.randint(0, width), np.random.randint(0, heigth)) for i in
                        range(numberofAgents)]
        print()

    def draw(self, screen):
        for i in range(self.numAgents):
            pygame.draw.circle(screen, self.dancers[i].getColor(), (self.dancers[i].posX, self.dancers[i].posY), 10)

    def updateDancers(self):
        """
        Changes the dancers' (agents) like rates
        """
        for dancer in self.dancers:
            neighbours = []
            for peer in self.dancers:
                if dancer == peer:
                    continue
                if (self.calculateDistance(dancer.posX,peer.posX,dancer.posY,peer.posY) < 100):
                    neighbours.append(peer)
            dancer.updatePosistion(neighbours,self.width,self.heigth)

    def calculateDistance(self,x1,x2,y1,y2):
        return np.sqrt(np.power(x1 - x2, 2) + np.power(y1 - y2, 2))

    def getDancersVotes(self, genre):
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
