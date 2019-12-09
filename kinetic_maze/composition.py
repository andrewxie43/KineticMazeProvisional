from .tracker import Tracker
from .physics import KineticMazeMotor
from .config import global_config as c
from . import logger
from . import tas
import os
import math

import pygame
from pygame.locals import *
import time

import threading


from .highscores import Scoreboard


TAS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tas.json")
l = logger.getChild("composition")

t = Tracker()

class KineticMaze:
    def __init__(self):
        self.kmm = None

    def hardware_setup(self):
        l.info("Initializing KineticMazeMotor")
        #self.kmm = KineticMazeMotor()
        l.info("Done initializing KineticMazeMotor")

    def run(self):

        '''
        try:
            f=open("../highscores.txt","r")
            f.close()
        except:
            print("No score file detected, random sample will be created.") #potentially merge this with other functions by using +
            sb.createBlank()
            sb.orderScores()
        '''

        l.info("Starting main loop")
        #Vars
        timer_on = False
        firstRun = True

        for angle in t.stream(): #Main loop!
            if angle is not None:
                if t.returnY("LEFT_HAND") < t.returnY("LEFT_ELBOW") and t.returnY("RIGHT_HAND") < t.returnY("RIGHT_ELBOW"):
                    l.debug("Got angle: %1.2f", angle)
                    print("Got angle:", math.radians(angle))
                    #sw.updateTimer(firstTime,timer_on)
                    self.kmm.set_velocity(self.kmm.adjust_angle(math.radians(angle)))
                else:
                    print("Hands not above elbow")
            else:
                self.kmm.set_velocity(self.kmm.ramp_down())
                l.debug("No user detected")
                print("No user detected")
                #sw.updateTimer(firstTime,timer_on)
