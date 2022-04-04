from math import cos, pi, sin
import matplotlib.pyplot as plt
import random
class PLANT:
    def __init__(self, string, dictionary, n, deltaTheta):
        for i in range(n):
            for i in range(len(string)):
                string = list(string)
                if string[i] in dictionary.keys():
                    string[i] = dictionary[string[i]]
                newstring = ""   
            for x in string:
                newstring += x
            string = newstring
        PLANT.str = string
        PLANT.dT = deltaTheta * pi / 180
    def drawPlant(self):
        currPt = (200,0)
        theta = (pi/2)
        stack = []
        for g in PLANT.str:
            colors = ['red','blue']
            RNG = random.randint(0,1)
            if g.isalpha():
                nextPt = (currPt[0]+cos(theta), currPt[1]+sin(theta))
                plt.plot([currPt[0],nextPt[0]],[currPt[1],nextPt[1]],color=colors[RNG])
                currPt = nextPt   
            elif g == "[":
                stack.append(currPt)
                stack.append(theta) 
            elif g == "]":           
                theta = stack.pop()
                currPt = stack.pop()
            elif g == "+":
                theta += PLANT.dT
            elif g == "-":
                theta -= PLANT.dT            
if __name__ == "__main__":
    myPlant=PLANT(input())
    myPlant.drawPlant()
    plt.axis('image')
    plt.show()