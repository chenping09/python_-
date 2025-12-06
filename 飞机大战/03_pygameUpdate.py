
import pygame
pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)
#游戏循环
while True:
    #指定循环体内部的代码的执行频率
    clock.tick(60)
    #捕获事件
    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)
    #事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            #卸载所有的模块
            pygame.quit()
            #终止当前执行的程序
            exit()

    #修改飞机的位置
    hero_rect.y -= 1
    #判断飞机的位置
    if hero_rect.y < 0:
        hero_rect.y = 700

    #调用blit方法的绘制
    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)

    #调用update方法的更新提示
    pygame.display.update()

pygame.quit()