'''
High Scores:
Implement a high score storage and retrieval system.
Does Pygame work with touchscreens?

If not, will need to rewrite display.py and composition.py to register touch

Score format: Name/Score
'''

import math
import time
import random
import numpy



#NTS: grab a square monitor
#TODO: Make checkscores call a GUI dialog box ffrom display.py or something. - USE KIVY!!!!! (screw tkinter)


#Vars
scorepath = "./highscores.txt" #c

samplePlaceholder = ["Alfa","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whisky","Xray","Yankee","Zulu"]
sampleMaleNames = ["Liam","Noah","William","James","Oliver","Benjamin","Elijah","Lucas","Mason","Logan","Alexander","Ethan","Jacob","Michael","Daniel","Henry","Jackson","Sebastian","Aiden","Matthew","Samuel","David","Joseph","Carter","Owen"]
sampleFemaleNames = ["Emma","Olivia", "Ava", "Isabella","Sophia","Charlotte","Mia","Amelia","Harper","Evelyn","Abigail","Emily","Elizabeth","Mila","Ella","Avery","Sofia","Camila","Aria","Scarlett","Victoria","Madison","Luna","Grace","Chloe"]
#names taken from the top 25 most popular baby names of 2018 and the NATO phonetic alphabet

#Need to interface with game, check if score in HS.

class Scoreboard:
    def __init__(self):
        try:
            f=open(scorepath,"r")
            f.close()
        except:
            self.createBlank()
        with open(scorepath) as f:
            first = f.read(1)
            if not first:
                self.genScores(10)
        self.orderScores()
    def createBlank(self): #Create a blank scoreboard in the folder before this
        f=open(scorepath,"a")
        f.close()
    def addEntry(self,name,score): #Add new entry at end
        f=open(scorepath,"a")
        f.write("{}/{}/\n".format(name, score))
    def getTop(self,number): #Get top number of high Scores, range!
        names = []
        scores = []

        f=open(scorepath,"r")
        lines = f.readlines()
        read = lines[0:number]

        for x in read:
            name = x.split("/")[0]
            score = x.split("/")[1]
            names.append(name)
            scores.append(score)

        return names,scores
    def getEntry(self, number): #get the number'th scoreboard
        f=open(scorepath,"r")

        lines = f.readlines()
        read = lines[number-1]

        name = read.split("/")[0]
        score = read.split("/")[1]

        return name,score
    def deleteEntry(self, number): #Delete a certain element
        with open(scorepath,"r") as f:
            lines = f.readlines()

        lines.pop(number-1)

        with open(scorepath, "w") as f:
            for line in lines:
                f.write(line)
    def secToDisp(self, secs): #convert seconds to displayable time, ASSUMING LESS THAN ONE HOUR
        mins = 0
        sec = secs
        while sec >= 60:
            mins += 1
            sec -= 60
        return "{}:{:02d}".format(mins,sec)
    def genScores(self, number): #mass generate number scores
        random.seed()
        for x in range(0,number):
            value = random.randint(0,1)
            if value == 0:
                name = random.choice(sampleMaleNames) + random.choice(samplePlaceholder)
            if value == 1:
                name = random.choice(sampleFemaleNames) + random.choice(samplePlaceholder)
            score = random.randint(300,600)
            self.addEntry(name,score)
    def orderScores(self): #reorder highscores from most to least

        scores = []
        with open(scorepath,"r") as f:
            lines = f.readlines()

        for x in lines:
            name = x.split("/")[0]
            score = x.split("/")[1]
            scores.append([name,int(float(score))])

        sort = sorted(scores, key=lambda x: x[1])

        parsed = []
        for arr in sort:
            par = "/".join([arr[0],str(arr[1]),"\n"])
            parsed.append(par)

        with open(scorepath, "w") as f:
            index = 0
            for line in lines:
                f.write(parsed[index])
                index+=1
    def checkScores(self,score,number): #Check if a score falls into the top X amount of scores, and adds to list if it is.
        check = False
        self.orderScores()
        name,scoir = self.getEntry(number)
        if score < int(scoir): #less score is better
            check = True

        if check == True:
            name = input("INPUT NAME: ")
            self.addEntry(name, score)
            self.orderScores()
        else:
            pass
    def getTotal(self): #get the amount of scores in the list
        total = 0
        with open(scorepath,"r") as f:
            lines = f.readlines()
        for item in lines:
            total += 1
        return total
    def getRanking(self, score): #Check where a score would fall on the scoreboard.
        scores = []
        self.orderScores()

        rank = 1

        with open(scorepath,"r") as f:
            lines = f.readlines()

        for x in lines:
            scoir = int(x.split("/")[1])
            if scoir < score:
                rank += 1
            else:
                break
        return rank
    #ALL ABOVE FUNCTIONS TESTED
