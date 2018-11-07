
import numpy as np


class Agent:

    def __init__(self):
        #Define the parameters of the agent
        random = np.random.uniform(0,1,3)
        s = np.sum(random)
        random = random / s
        self.rock = random[0]
        self.pop = random[1]
        self.techno = random[2]

    def getTaste(self):
        _tmp = [self.rock,self.pop,self.techno]
        _max = _tmp.index(max(_tmp))
        if _max == 0:
            return "ROCK"
        if _max == 1:
            return "POP"
        if _max == 2:
            return "TECHNO"
        else:
            return "ERROR"

    def getColor(self):
        taste = self.getTaste()
        if taste == "ROCK":
            return (255,0,0)
        if taste == "POP":
            return (0,255,0)
        if taste == "TECHNO":
            return (0,0,255)
        else:
            return (0,0,0)

    def getLikeRate(self,genre):
        if genre == "ROCK":
            return self.rock
        if genre == "POP":
            return self.pop
        if genre == "TECHNO":
            return self.techno
        else:
            return 0

    #Behaviour formulas

    def getInfluenceFactor(self,genre):
        return 0.25 * self.getLikeRate(genre) + 0.25 * np.random.uniform(0,1)

    def calculateNewLikeRates(self,neighbours):
        for neighbour in neighbours:
            nTaste = neighbour.getTaste()
            if nTaste == "ROCK":
                self.rock = 0.5 * self.rock + neighbour.getInfluenceFactor(nTaste)
                self.pop = self.pop - neighbour.getInfluenceFactor(nTaste) / 2
                self.techno = self.techno - neighbour.getInfluenceFactor(nTaste) / 2
            if nTaste == "POP":
                self.pop = 0.5 * self.pop + neighbour.getInfluenceFactor(nTaste)
                self.rock = self.rock - neighbour.getInfluenceFactor(nTaste) / 2
                self.techno = self.techno - neighbour.getInfluenceFactor(nTaste) / 2
            if nTaste == "TECHNO":
                self.techno = 0.5 * self.techno + neighbour.getInfluenceFactor(nTaste)
                self.pop = self.pop - neighbour.getInfluenceFactor(nTaste) / 2
                self.rock = self.rock - neighbour.getInfluenceFactor(nTaste) / 2