import pygame
import sys
from pygame.locals import *
from bullet import Bullet
from alien import Alien
from time import sleep
import music

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    if event.key==pygame.K_LEFT:
        ship.moving_left=True
    if event.key==pygame.K_UP:
        ship.moving_up=True
    if event.key==pygame.K_DOWN:
        ship.moving_down=True
    if event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
        music.shooting_sound.play()
    if event.key==pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    
        
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
    if event.key==pygame.K_UP:
        ship.moving_up=False
    if event.key==pygame.K_DOWN:
        ship.moving_down=False

       
def check_events(ai_settings,screen,stats,sb,ship,bullets,play_button,aliens):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
                
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)


def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y): 

    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:  #在玩家单击按钮play时开始新游戏
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()  #重置游戏统计信息
        stats.game_active=True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        aliens.empty()
        bullets.empty()
        add_aliens(ai_settings,screen,aliens)
        ship.center_ship()
    

                           
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):

    screen.fill(ai_settings.bg_color)#每次循环时都会重绘屏幕
        
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
         play_button.draw_button()
    
    pygame.display.flip()  #让最近绘制的屏幕可见


def update_bullets(ai_settings,screen,stats,sb,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():  #删除子弹
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(ai_settings,screen,stats,sb,bullets,aliens)
    

def check_bullets_aliens_collisions(ai_settings,screen,stats,sb,bullets,aliens):  #检查子弹与外星人碰撞
    
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:
        music.bomb_sound.play()
        stats.score+=ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats,sb)
        
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()

        stats.level+=1  #提升等级
        sb.prep_level()

        add_aliens(ai_settings,screen,aliens)
        
        
    
def add_aliens(ai_settings,screen,aliens):  #创建外星人
    number=20
    for i in range(number):
        alien=Alien(ai_settings,screen)
        aliens.add(alien)

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1

        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        add_aliens(ai_settings,screen,aliens)
        ship.center_ship()
    
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):  #飞船与外星人碰撞
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens,pygame.sprite.collide_mask):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)


def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
    
        
        



    
    
