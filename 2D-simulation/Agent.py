import datetime
import random
import uuid
import numpy as np
import json


class Agent:

    def __init__(self, username, posX, posY):
        # Define the parameters of the agent
        random = np.random.uniform(0, 1, 3)
        s = np.sum(random)
        random = random / s
        self.rock = random[0]
        self.pop = random[1]
        self.techno = random[2]

        self.username = username
        self.uid = uuid.uuid4()

        self.posX = posX
        self.posY = posY

        self.speed = 1

    def getTaste(self):
        _tmp = [self.rock, self.pop, self.techno]
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
            return (255 * self.rock, 0, 0)
        if taste == "POP":
            return (0, 255 * self.pop, 0)
        if taste == "TECHNO":
            return (0, 0, 255 * self.techno)
        else:
            return (0, 0, 0)

    def getLikeRate(self, genre):
        if genre == "ROCK":
            return self.rock
        if genre == "POP":
            return self.pop
        if genre == "TECHNO":
            return self.techno
        else:
            return 0

    # Behaviour formulas

    def getInfluenceFactor(self, genre):
        return 0.25 * self.getLikeRate(genre) + 0.25 * np.random.uniform(0, 1)

    def updatePosistion(self, neighbours,max_w,max_h):
        """
        Defines the behaviour of the agent
        Calculate the new likerates based on the neighbours"s most liked genre
        :param neighbours: a list with neighbour agents
        :return: nothing
        """
        random.shuffle(neighbours)

        # Update the position of the dancer based on his like rate
        for neighbour in neighbours:
            A = [self.rock,self.pop,self.techno]
            B = [neighbour.rock,neighbour.pop,neighbour.techno]
            mse = np.sum(np.power(np.asarray(A) - np.asarray(B),2))* 1 / len(A)
            print(mse * 100)

            try:
                if mse*100 < 5 :
                    dirX = self.posX - neighbour.posX
                    dirY = self.posY - neighbour.posY
                else:
                    dirX = (self.posX - neighbour.posX) * -1
                    dirY = (self.posY - neighbour.posY) * -1

                if dirX == 0 and dirY == 0: #Collision
                    self.posX = self.posX + np.random.randint(-20,20)
                    self.posY = self.posY + np.random.randint(-20,20)
                self.posX += self.speed * np.sign(dirX) * -1
                self.posY += self.speed * np.sign(dirY) * -1
            except:
                pass

        #Stay between the boundries of the screen
        if self.posX > max_w:
            self.posX = max_w
        if self.posX < 0:
            self.posX = 0
        if self.posY > max_h:
            self.posY = max_h
        if self.posY < 0:
            self.posY = 0


def vote(self, genre):
    """
    :return: json string : the vote message
    """
    if self.getTaste() == genre:
        return json.dumps({"timestamp": datetime.datetime.now().isoformat(),
                           "value": 1,
                           "username": str(self.username),
                           "uid": str(self.uid),
                           "songid": 0})
    else:
        return json.dumps({"timestamp": datetime.datetime.now().isoformat(),
                           "value": -1,
                           "username": str(self.username),
                           "uid": str(self.uid),
                           "songid": 0})
