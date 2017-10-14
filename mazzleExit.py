from Tkinter import *
from random import *
import time
import numpy as np
import util

class Directions:
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'

# Detect elements in the map



window = Tk()
window.title('CityBusPlanner')
window.resizable(0,0)
width = 25
(x, y) = (22, 22)

totalsteps = 0

buidings = [(0, 0), (1, 0), (2, 0), (3, 0), (7, 0), (8, 0), (11, 0), (12, 0), (13, 0),
            (17, 0), (18, 0), (21, 0), (21, 1), (2, 2), (5, 2), (8, 2), (9, 2), (12, 2),
            (14, 2), (15, 2), (16, 2), (17, 2), (21, 2), (2, 3), (4, 3), (5, 3), (7, 3),
            (8, 3), (11, 3), (17, 3), (18, 3), (19, 3), (2, 4), (4, 4), (5, 4), (8, 4),
            (9, 4), (14, 4), (15, 4),(17, 4), (18, 4), (19, 4), (0, 6), (2, 6), (4, 6),
            (7, 6), (8, 6), (11, 6), (12, 6), (14, 6), (15, 6),(16, 6), (18, 6), (19, 6),
            (2, 7), (5, 7), (21, 7), (0, 8), (2, 8), (11, 8), (14, 8), (15, 8), (17, 8),
            (18, 8), (21, 8), (4, 9), (5, 9), (7, 9), (9, 9), (11, 9), (14, 9), (21, 9),
            (2, 10), (7, 10), (14, 10), (17, 10), (19, 10), (0, 11), (2, 11), (4, 11),
            (5, 11), (7, 11), (8, 11), (9, 11), (11, 11), (12, 11), (14, 11), (15, 11),
            (16, 11), (17, 11), (18, 11), (19, 11), (0, 13), (2, 13), (3, 13), (5, 13),
            (7, 13), (8, 13), (9, 13), (14, 13), (17, 13), (18, 13), (21, 13), (2, 14),
            (3, 14), (5, 14), (7, 14),(9, 14), (12, 14), (14, 14), (15, 14), (17, 14),
            (18, 14), (21, 14), (2, 15), (3, 15), (5, 15), (7, 15), (9, 15), (12, 15),
            (15, 15), (19, 15), (21, 15), (0, 16), (21, 16), (0, 17), (3, 17), (5, 17),
            (7, 17),(9, 17), (11, 17), (14, 17), (15, 17), (17, 17), (18, 17), (21, 17),
            (2, 18), (3, 18), (5, 18), (7, 18),(9, 18), (11, 18), (14, 18), (17, 18),
            (18, 18), (3, 19), (5, 19), (7, 19), (9, 19), (11, 19), (12, 19), (14, 19),
            (17, 19), (18, 19), (0, 21), (1, 21), (2, 21), (5, 21), (6, 21), (9, 21),
            (10, 21), (11, 21), (12, 21), (15, 21), (16, 21), (18, 21), (19, 21), (21, 21)]

walls = [(10, 0), (0, 12), (21, 12), (14, 21)]
park = [(14, 0), (15, 0), (16, 0)]
robotPos = (21, 12)

view = Canvas(window, width=x * width, height=y * width)
view.grid(row=0, column=0)
searchMapButton = Button(window,text = 'search')
searchMapButton.grid(row = 0,column = 1)
robotView = Canvas(window,width=x * width, height=y * width)
robotView.grid(row = 0,column = 2)

def formatColor(r, g, b):
    return '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))

def cityMap():
    global width, x, y, buidings,walls,park,robot
    for i in range(x):
        for j in range(y):
            view.create_rectangle(
                i * width, j * width, (i + 1) * width, (j + 1) * width, fill='white', outline='gray', width=1)
    for (i, j) in buidings:
        view.create_rectangle(
            i * width, j * width, (i + 1) * width, (j + 1) * width, fill='black', outline='gray', width=1)
    for (i,j) in walls:
        view.create_rectangle(
            i * width, j * width, (i + 1) * width, (j + 1) * width, fill='blue', outline='gray', width=1)
    for (i,j) in park:
        view.create_rectangle(
            i * width, j * width, (i + 1) * width, (j + 1) * width, fill='red', outline='gray', width=1)

def robotCityMap():
    global width, x, y, buidings,walls,park,robot,robotPos
    for i in range(x):
        for j in range(y):
            robotView.create_rectangle(
                i * width, j * width, (i + 1) * width, (j + 1) * width, fill='black', width=1)
    robotView.create_rectangle(
                robotPos[0] * width, robotPos[1] * width, (robotPos[0] + 1) * width, (robotPos[1] + 1) * width, fill='white', outline='gray', width=1)
# Create City Map
cityMap()

# Create Robot View
robotCityMap()
# Create a robot
robot = view.create_rectangle(robotPos[0] * width + width * 2 / 10, robotPos[1] * width + width * 2 / 10,
                            robotPos[0] * width + width * 8 / 10, robotPos[1] * width + width * 8 / 10, fill="orange", width=1, tag="robot")
robotSelf = robotView.create_rectangle(robotPos[0] * width + width * 2 / 10, robotPos[1] * width + width * 2 / 10,
                            robotPos[0] * width + width * 8 / 10, robotPos[1] * width + width * 8 / 10, fill="orange", width=1, tag="robot")

visited = [robotPos]

window.bind("<Up>", callUp)
window.bind("<Down>", callDown)
window.bind("<Right>", callRight)
window.bind("<Left>", callLeft)
window.bind("s", searchMap)
searchMapButton.bind("<Button-1>",searchMap)
window.mainloop()
