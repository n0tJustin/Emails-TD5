import math

def getCoords():
   coords=[]
   coord1, x, y = goRight(-20, 66, 63)
   coords.extend(coord1)

   coord2, x, y = goDown(x, y, 28)
   coords.extend(coord2)

   coord3, x, y = goRight(x, y, 37)
   coords.extend(coord3)

   coord4, x, y = goUp(x, y, 29, swing=5)
   coords.extend(coord4)

   coord5, x, y = goRight(x, y, 40)
   coords.extend(coord5)

   coord6, x, y = goDown(x, y, 60, swing=5)
   coords.extend(coord6)

   coord7, x, y = goLeft(x, y, 39)
   coords.extend(coord7)

   coord8, x, y = goDown(x, y, 59, swing=4)
   coords.extend(coord8)

   coord9, x, y = goRight(x, y, 40)
   coords.extend(coord9)

   coord10, x, y = goUp(x, y, 29, swing=4)
   coords.extend(coord10)

   coord11, x, y = goRight(x, y, 36, swing=5)
   coords.extend(coord11)

   coord12, x, y = goDown(x, y, 27, swing=4)
   coords.extend(coord12)

   coord13, x, y = goRight(x, y, 63)
   coords.extend(coord13)

   return coords

def goRight(x, y, distance, pace = 3, swing=8):
   coord1 = []
   starty = y
   for index in range(distance):
       x += pace
       y = starty + swing * abs(math.sin(index/10))
       t = (x, y)
       coord1.append(t)
   return coord1, x, y

def goDown(x, y, distance, pace = 3, swing=8):
   coord1 = []
   startx = x
   for index in range(distance):
       y += pace
       x = startx + swing * abs(math.sin(index/10))
       t = (x, y)
       coord1.append(t)
   return coord1, x, y

def goUp(x, y, distance, pace = 3, swing=8):
   coord1 = []
   startx = x
   for index in range(distance):
       y -= pace
       x = startx + swing * abs(math.sin(index/10))
       t = (x, y)
       coord1.append(t)
   return coord1, x, y

def goLeft(x, y, distance, pace = 3, swing=8):
   coord1 = []
   starty = y
   for index in range(distance):
       x -= pace
       y = starty + swing * abs(math.sin(index/10))
       t = (x, y)
       coord1.append(t)
   return coord1, x, y

