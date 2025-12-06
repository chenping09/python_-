import pygame
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点" + f'{hero_rect.x} {hero_rect.y}')
print("英雄的尺寸" + f'{hero_rect.width} {hero_rect.height}')
print(f'{hero_rect.size}')