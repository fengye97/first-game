import pygame
from pygame.sprite import Sprite
from random import *

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        
        
        self.image=pygame.image.load('images/alien.png')
        self.rect=self.image.get_rect()
        self.width,self.height=ai_settings.screen_width,ai_settings.screen_height
        self.rect.left,self.rect.top=\
                                       randint(0,self.width-self.rect.width),\
                                       randint(-5*self.height,0)
        
         

    def update(self):
        if self.rect.top<self.height:
            self.rect.top+=self.ai_settings.alien_speed_factor
        else:
            self.reset()


    def reset(self):
        self.rect.left,self.rect.top=\
                                       randint(0,self.width-self.rect.width),\
                                       randint(-5*self.height,0)

   
