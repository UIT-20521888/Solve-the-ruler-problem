class Text:
    def __init__(self,text="",font=None,color=None,point=None):
        self.text = font.render(text,True,color)# color text
        self.rect=self.text.get_rect()#position of box
        self.rect.center = point# position of box in center
    #display text on screen
    def draw(self, screen):
        screen.blit(self.text,self.rect)