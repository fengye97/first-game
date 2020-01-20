import pygame
import sys
from pygame.locals import *
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():   
    pygame.init()  #初始化背景设置
    pygame.mixer.init()

    pygame.mixer.music.load("bgm_music.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1,0.0)


    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,\
                                    ai_settings.screen_height)) 

                                        #创建一个窗口
    pygame.display.set_caption("Alien Invasion")
    play_button=Button(ai_settings,screen,"Play")
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    gf.add_aliens(ai_settings,screen,aliens)
  

    while True:
        gf.check_events(ai_settings,screen,stats,sb,ship,bullets,play_button,aliens)#检查玩家的输入

        if stats.game_active:   
            ship.update()                                   #更新飞船的位置
            gf.update_bullets(ai_settings,screen,stats,sb,aliens,bullets)      #所有未消失的子弹的位置                                    
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)  #(错误:缺少ai_settings)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)  #更新屏幕(错误：缺少一个形参alien)

        

run_game()


  
 
