import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()


shooting_sound=pygame.mixer.Sound("shooting.ogg")
shooting_sound.set_volume(0.2)
bomb_sound=pygame.mixer.Sound("bomb.ogg")
bomb_sound.set_volume(0.2)
