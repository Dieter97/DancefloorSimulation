import datetime
import uuid
import numpy as np
import json

class Agent:

    def __init__(self,username):
        #Define the parameters of the agent
        random = np.random.uniform(0,1,3)
        s = np.sum(random)
        random = random / s
        self.rock = random[0]
        self.pop = random[1]
        self.techno = random[2]

        self.username = username
        self.uid = uuid.uuid4()


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
            return (255 * self.rock,0,0)
        if taste == "POP":
            return (0,255 * self.pop,0)
        if taste == "TECHNO":
            return (0,0,255 * self.techno)
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
        """
        Defines the behaviour of the agent
        Calculate the new likerates based on the neighbours"s most liked genre
        :param neighbours: a list with neighbour agents
        :return: nothing
        """
        for neighbour in neighbours:
            nTaste = neighbour.getTaste()
            influencFactor = neighbour.getInfluenceFactor(nTaste)
            if nTaste == "ROCK":
                self.rock = 0.5 * self.rock + influencFactor
                self.pop = self.pop - influencFactor / 2
                self.techno = self.techno - influencFactor / 2
            if nTaste == "POP":
                self.pop = 0.5 * self.pop + influencFactor
                self.rock = self.rock - influencFactor / 2
                self.techno = self.techno - influencFactor / 2
            if nTaste == "TECHNO":
                self.techno = 0.5 * self.techno + influencFactor
                self.pop = self.pop - influencFactor / 2
                self.rock = self.rock - influencFactor / 2

        #Limit the values
        if self.rock < 0:
            self.rock = 0
        if self.pop < 0:
            self.pop = 0
        if self.techno < 0:
            self.techno = 0
        #print(self.rock+self.pop+self.techno)


    def vote(self,genre):
        """
        :return: json string : the vote message
        """
        if self.getTaste() == genre:
            return json.dumps({"timestamp":datetime.datetime.now().isoformat(),
                       "value": 1,
                       "username": str(self.username),
                       "uid": str(self.uid),
                       "songid":0})
        else:
            return json.dumps({"timestamp":datetime.datetime.now().isoformat(),
                       "value": -1,
                       "username": str(self.username),
                       "uid": str(self.uid),
                       "songid":0})