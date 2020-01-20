import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        

        self.image=pygame.image.load('images/ship.png')#加载飞船图像并获得其外接矩形
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx  #将飞船放在屏幕中央 
        self.rect.bottom=self.screen_rect.bottom-20
        
        
        self.x=float(self.rect.centerx)  #在飞船的属性x中存储小数值
        self.y=float(self.rect.bottom)
        
        self.moving_right=False  #移动标志
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
         
       
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x +=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.x -=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
            self.y -=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y +=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.x
        self.rect.bottom=self.y
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def center_ship(self):
        self.rect.centerx=self.screen_rect.centerx  #将飞船放在屏幕中央 
        self.rect.bottom=self.screen_rect.bottom-20
        
        
    
