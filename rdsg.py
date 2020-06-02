#!/usr/bin/python2
from io import BytesIO 
import pygame
import time
from pygame.locals import *
import random

class krand:
    def __init__(self, n):
        self.N = n
        self.ini(n)

    def ini(self, n):
        self.ns = [0]*n
        for i in range(n):
            self.ns[i] = i
        random.shuffle(self.ns)

    def rnd(self):
        i = self.ns.pop(0)
        if len(self.ns) == 0:
            self.ini(self.N)
        return(i)

    def __del__(self):
        self.ns = []
        self.N = 1


pygame.init()
filename = 'stereogram.jpg'
# image size 534x308
xsize=534
ysize=308
screen=pygame.display.set_mode((xsize,ysize),0,32)
img=pygame.image.load(filename).convert()
surface=pygame.Surface((xsize,ysize))

r=krand(xsize*ysize)
surface.blit(img,(0,0))
for cnt in range(xsize*ysize):
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
  p=r.rnd()
  px,py=divmod(p,ysize)
  pos=(px,py)
  col=surface.get_at(pos)
  screen.set_at(pos,col)
  pygame.display.update()

time.sleep( 20 )
