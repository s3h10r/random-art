#!/usr/bin/env python3
import math
import random
import sys
from PIL import Image


class X:
   def eval(self, x, y):
      return x

   def __str__(self):
      return "x"

class Y:
   def eval(self, x, y):
      return y

   def __str__(self):
      return "y"

class SinPi:
   def __init__(self, prob):
      self.arg = buildExpr(prob * prob)

   def __str__(self):
      return "sin(pi*" + str(self.arg) + ")"

   def eval(self, x, y):
      return math.sin(math.pi * self.arg.eval(x,y))

class CosPi:
   def __init__(self, prob):
      self.arg = buildExpr(prob * prob)

   def __str__(self):
      return "cos(pi*" + str(self.arg) + ")"

   def eval(self, x, y):
      return math.cos(math.pi * self.arg.eval(x,y))

class Times:
   def __init__(self, prob):
      self.lhs = buildExpr(prob * prob)
      self.rhs = buildExpr(prob * prob)

   def __str__(self):
      return str(self.lhs) + "*" + str(self.rhs)

   def eval(self, x, y):
      return self.lhs.eval(x,y) * self.rhs.eval(x,y)

def buildExpr(prob = 0.99):
   if random.random() < prob:
      return random.choice([SinPi, CosPi, Times])(prob)
   else:
      return random.choice([X, Y])()

def plotIntensity(exp, pixelsPerUnit = 150):
    canvasWidth = 2 * pixelsPerUnit + 1
    canvas = Image.new("L", (canvasWidth, canvasWidth))

    for py in range(canvasWidth):
        for px in range(canvasWidth):
            # Convert pixel location to [-1,1] coordinates
            x = float(px - pixelsPerUnit) / pixelsPerUnit
            y = -float(py - pixelsPerUnit) / pixelsPerUnit
            z = exp.eval(x,y)

            # Scale [-1,1] result to [0,255].
            intensity = int(z * 127.5 + 127.5)
            canvas.putpixel((px,py), intensity)

    return canvas

def plotColor(redExp, greenExp, blueExp, pixelsPerUnit = 150):
    redPlane   = plotIntensity(redExp, pixelsPerUnit)
    greenPlane = plotIntensity(greenExp, pixelsPerUnit)
    bluePlane  = plotIntensity(blueExp, pixelsPerUnit)
    return Image.merge("RGB", (redPlane, greenPlane, bluePlane))

def makeImage(numPics = 20, pixelsPerUnit = 150):
   with open("eqns.txt", 'w') as eqnsFile:
      for i in range(numPics):
         redExp = buildExpr()
         greenExp = buildExpr()
         blueExp = buildExpr()

         eqnsFile.write("img" + str(i) + ":\n")
         eqnsFile.write("red = " + str(redExp) + "\n")
         eqnsFile.write("green = " + str(greenExp) + "\n")
         eqnsFile.write("blue = " + str(blueExp) + "\n\n")

         image = plotColor(redExp, greenExp, blueExp, pixelsPerUnit)
         image.save("img" + str(i) + ".png", "PNG")

def generate_image(pixels_per_unit = 150, rand_seed = None):
    """
    allows calling from external code (e.g. polaroidme)

    return PilImage, meta (string)
    """
    seed = rand_seed
    if not seed:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)
    redExp = buildExpr()
    greenExp = buildExpr()
    blueExp = buildExpr()
    image = plotColor(redExp, greenExp, blueExp, pixels_per_unit)
    meta = 'red={} green={} blue={} seed={}'.format(redExp,greenExp,blueExp,seed)
    return image, meta

if __name__ == '__main__':
    amount = 50
    pixelsPerUnit = 150
    seed = random.randrange(sys.maxsize)
    if len(sys.argv) > 1:
        amount = int(sys.argv[1])
    if len(sys.argv) > 2:
        pixelsPerUnit = int(sys.argv[2])
    if len(sys.argv) > 3:
        seed = int(sys.argv[3])
    print("amount: %i ppu: %i seed: %i" % (amount,pixelsPerUnit,seed))
    random.seed(seed)
    makeImage(amount, pixelsPerUnit)
