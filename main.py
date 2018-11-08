import re
import time

import pygame
import sys

from Grid import Grid
from mqtt import mqtt


#Variables
width,height = 200,200
rect_width=10
genre = "ROCK" #Init the genre currently playing

# connecteer met mqtt op host *.101 en poort 1883
mqttclient = mqtt("broker.mqttdashboard.com", 1883)
grid = "" #Initialze the grid variable to empty string

#Bereid scherm voor op visualisatie van automata
def visualize_dancefloor():
    global grid
    #initializeer pygame scherm met size 500x500 pixels
    pygame.init()
    screen=pygame.display.set_mode((width*rect_width,height*rect_width))
    #teken een vierkant op het scherm op positie x=0,y=0 met een breedte van 10
    grid = Grid(width,height)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()

        grid.draw(screen,rect_width,rect_width)
        grid.updateDancers()

        # refresh scherm
        pygame.display.update()

        #time.sleep(0.5)

#Connecteer met Mqtt Host
def start_dj_listener():
    mqttclient.connect()
    mqttclient.add_listener_func(on_dj_message)

#Wordt opgeroepen wanneer er een Mqtt bericht binnenkomt
def on_dj_message(msg):
    global genre, grid
    genre = re.search("'(.*)'", msg).group(1)
    print("Message received: "+str(genre))
    # Send the vote messages
    for vote in grid.getDancersVotes(genre):
        mqttclient.publish("votes/", vote)

start_dj_listener()
visualize_dancefloor()