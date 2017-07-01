import sys
import os
from time import sleep
from copy import deepcopy

aliveChar = '@'
deadChar = ' '

def alive_dead(x, y):
    if plane[y][x] == aliveChar:
        return True
    return False

def moore(x, y):
    neighbour = 0

    for yplane in range(-1, 2):
        for xplane in range(-1, 2):
            if (xplane != 0) or (yplane != 0):
                if (x + xplane >= 0) and (y + yplane >= 0) and (x + xplane < width) and (y + yplane < height):
                    if alive_dead(x + xplane, y + yplane):
                        neighbour += 1
    
    return neighbour

def printPlane(planeArg):
    for y in range(0, height):
        for x in range(0, width):
            sys.stdout.write(planeArg[y][x])
        print()

width = int(input("Width of plane: "))
height = int(input("Height of plane: "))
slp = float(input("Sleep: "))

nf = input("Create new configuration file? y/n : ")

if nf == "y":
    planePrimary = open("./plane", "w")

    for y in range(0, height - 1):
        for x in range(0, width):
            planePrimary.write(".")
        planePrimary.write("\n")

    for x in range(0, width):
        planePrimary.write(".")

    planePrimary.close()

os.system("clear")

input("Change the primary cell configuration in 'plane'. '@' -> Living cell. '.' -> Dead cell. Press Enter...")

os.system("clear")

with open("./plane", "r") as planefile:
    planePrimary = planefile.read().split("\n")

for i in range(0, len(planePrimary)):
    if len(planePrimary[i]) != width:
        break

if i != height - 1:
    print("Wrong cell configuration!")
    sys.exit(0)

plane = [['.' for x in range(width)] for y in range(height)] 

for y in range(0, height):
    for x in range(0, width):
        if planePrimary[y][x] == '.':
            plane[y][x] = deadChar
        else:
            plane[y][x] = aliveChar

#PRIMARY CONFIG
printPlane(plane)
input()

os.system("clear")

run = 0

#BEHAVIOUR
while True:
    newplane = deepcopy(plane)

    for y in range(0, height):
        for x in range(0, width):
            alive = alive_dead(x, y)

            #RULES
            if (alive == False) and (moore(x, y) == 3):
                newplane[y][x] = aliveChar

            elif (alive == True) and ((moore(x, y) == 1) or (moore(x, y) > 3)):
                newplane[y][x] = deadChar

            elif (alive == True) and (moore(x, y) == 0):
                newplane[y][x] = deadChar

            else:
                newplane[y][x] = plane[y][x]
    
    plane = deepcopy(newplane)
    
    os.system("clear")
    printPlane(plane)

    print()
    print(run)

    if slp != 0:
        sleep(slp)
    else:
        input()

    run += 1