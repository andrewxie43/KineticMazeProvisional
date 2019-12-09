'''
Kinetic Maze display:
controls everything that's displayed in the window.

'''




#Display a line at a given angle
import pygame
import math
import os
from pygame.locals import *
import time

#Make screen
SIZE = 800, 800 #POTENTIAL: Set all element to change location based off screen size?
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Kinetic Maze V2")
FPSCLOCK = pygame.time.Clock()
done = False
screen.fill((0, 0, 0))


#stopwatch setup
clock = pygame.time.Clock()

myfont = pygame.font.SysFont("monospace", 25)
fontSize = myfont.size("00:00:00")


class Liner:
    def __init__(self):
        pass



    def dispAngle(self, angle):

        linCover = pygame.surface.Surface((720,600)).convert()
        linCover.fill((0, 0, 0))
        screen.blit(linCover, (0,100))
        #Set max and min movement
        '''
        if (angle > 0.5):
            angle = 0.5
        elif (angle < -0.5):
            angle = -0.5
        '''
        degree = angle * 90 #adjust for kinect dampening, calibrate at some point!

        #screen.fill(0
        radar = (400,400)
        radar_len = 300
        x = radar[0] + math.cos(math.radians(degree)) * radar_len
        y = radar[1] + math.sin(math.radians(degree)) * radar_len

        x2 = radar[0] - math.cos(math.radians(degree)) * radar_len
        y2 = radar[1] - math.sin(math.radians(degree)) * radar_len

    #+0.5 to -0.5, 0.5 being 90 degrees left (pov of cam)

        # then render the line radar->(x,y)
        pygame.draw.line(screen, Color("red"), radar, (x,y), 5)
        pygame.draw.line(screen, Color("blue"), radar, (x2,y2), 5)
        pygame.display.flip()





class StopWatch:
    def __init__(self):
        pass

    def dispSW(self):
        initTimer = myfont.render("00:00", True, (255,255,255), (0,0,0))
        screen.blit(initTimer,(400 - (fontSize[0] / 2.), 700)) #Display blank timer
        pygame.display.update()

    def startTimer(self): #this return should beused as updateTimer's before Time
        return time.time()

    def updateTimer(self, beforeTime, timerStart): #Timer start used to stop timer

        if timerStart == False:
            return

        currentTime = time.time()
        cover = pygame.surface.Surface((160,40)).convert()
        cover.fill((0, 0, 0))

        seconds = currentTime - beforeTime
        minutes = 0
        while seconds >=60:

            minutes += 1
            seconds -= 60
            seconds += 1
            screen.blit(cover, (400 - (fontSize[0] / 2.), 700))
            pygame.display.update()



        timelabel = myfont.render("{:02d}:{:02d}".format(int(minutes), int(seconds)), True, (255,255,255), (0,0,0))
        screen.blit(timelabel,(400 - (fontSize[0] / 2.), 700))
        pygame.display.update()

    def stopTimer(self,beforeTime):
        #TODO: use beforetime for leaderboard, calculate elapsed seconds.
        self.dispSW()
        print("Time Elasped: %d seconds" %(time.time()-beforeTime))

class Buttons:
    def __init__(self):
        pass
    def draw(self,text, x, y, xcenter, ycenter, color):
        self.xcenter = xcenter #move to init?
        self.ycenter = ycenter
        self.x = x
        self.y = y

        pygame.draw.rect(screen,color,Rect(xcenter - (x/2), ycenter - (y/2), x, y)) #Draw Button

        newText = myfont.render(text, True, (0,0,255)) #Add text to buttons
        textSize = myfont.size(text)
        screen.blit(newText, (xcenter- (textSize[0] / 2.),ycenter - (textSize[1] / 2.)))
        pygame.display.update()
    def inBox(self): #if mouse in box

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (self.xcenter + self.x/2) > mouse[0] > (self.xcenter - self.x/2) and (self.ycenter + self.y/2) > mouse[1] > (self.ycenter - self.y/2):
                return True
class Spooky: #because skeletons are spooky, draws one frame of the skele based on inputs

            #3 numbers in each joint array.
            #1st is leftright
            #2nd is updown, higher is higher
            #3rd is depth, dist from camera


    def __init__(self):
        pass

    def updateSk(self, a, b, c, d, e, f, g):
        self.lh = a #left hand
        self.rh = b #right hand
        self.t = c #torso
        self.le = d #left elbow
        self.re = e #right elbow
        self.ls = f #left shoulder
        self.rs = g #right shoulder

    def angleTwoJoints(self,one,two):
        delta = two - one
        return math.atan2(delta[1], delta[0])

    def angleLine(self,startx,starty, angle): #draw a line at an angle with fixed start point
        end = startx + 5*math.cos(angle),starty + 5*math.sin(angle) #location of the nonfixed end
        pygame.draw.line(screen, Color("green"), (startx,starty), end, 5)
        pygame.display.update()

    #def returnEnd(self,startx,starty,angle):
        return (startx + 100*math.cos(math.radians(angle)),starty + 100*math.sin(math.radians(angle)))

    def returnLeftEnd(self,tuple,angle):
        startx, starty = tuple
        return (startx - 75*math.cos(math.radians(angle)),starty - 75*math.sin(math.radians(angle)))
        #image flipped?

    def returnRightEnd(self,tuple,angle):
        startx, starty = tuple
        return (startx - 75*math.cos(math.radians(angle)),starty - 75*math.sin(math.radians(angle)))
        #image flipped?

    def drawSkel(self): #untested as of 12/2/2019
        #The plan is to draw each line between joints as the same length, but change the angle of display and a fixed point. first fixed point will be the torso, at 0,0 or something

        linCover = pygame.surface.Surface((720,600)).convert()
        linCover.fill((0, 0, 0))
        screen.blit(linCover, (0,100))

        #pygame.draw.line(screen, Color("yellow"), (400,300), (400,500), 1)


        torso = (400,400)
        shoulder = self.returnLeftEnd(torso, self.angleTwoJoints(self.t,self.ls)  * 45)
        elbow = self.returnLeftEnd(shoulder, self.angleTwoJoints(self.ls,self.le)  * 45)
        hand = self.returnLeftEnd(elbow, self.angleTwoJoints(self.le,self.lh)  * 45)
        leftPoints = [shoulder, elbow, hand]

        pygame.draw.lines(screen, Color("green"), False, leftPoints)
        # left arm works-ish, shoulder line goes straight down but else tracks well.


        rshoulder = self.returnRightEnd(torso, self.angleTwoJoints(self.t,self.rs) * 45)
        relbow = self.returnRightEnd(rshoulder, self.angleTwoJoints(self.rs,self.re)  * 45)
        rhand = self.returnRightEnd(relbow, self.angleTwoJoints(self.re,self.rh)  * 45)
        rightPoints = [rshoulder, relbow, rhand]

        pygame.draw.lines(screen, Color("red"), False, rightPoints)

        pygame.draw.lines(screen, Color("blue"), True, [torso, shoulder, rshoulder])


        pygame.display.update()
