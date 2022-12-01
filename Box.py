import pygame as pg
# box display 
class BOX:
    def __init__(self,COLOR=(0,0,0),Rect=None,width=2):
        self.color =COLOR# color text
        self.rect = Rect# position of box
        self.width = width# dept box
    # display box on screen
    def draw(self,screen):
        pg.draw.rect(screen,self.color,self.rect,self.width)
